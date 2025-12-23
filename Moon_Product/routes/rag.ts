import express, { Request, Response } from 'express';
const router = express.Router();

import { text } from '../constants/text';

import {
	Document,
	VectorStoreIndex,
	ResponseSynthesizer,
	CompactAndRefine,
	Settings,
	OpenAI,
	TextQaPrompt,
} from 'llamaindex';
//must use node version 18 or higher for llamaindex to work

router.post('/', async (req: Request, res: Response) => {
	try {
		const { articleNumber, company, reason } = req.body;

		const query = `query: Given the supplier: ${company} or the reason for objection: ${reason} in context information and the enapoint number: ${articleNumber}, find and write the text of final agreement.`;
		Settings.llm = new OpenAI({ model: 'gpt-3.5-turbo', temperature: 0.1 });

		const document = new Document({ text: text, id_: 'text' });

		const newTextQaPrompt: TextQaPrompt = ({ context }) => {
			return `Context information is below.
        ---------------------
        ${context}
        ---------------------
        You are a purchasing officer in a company called MAN. You are leading negotiations with suppliers in automotive industry. 
        If none of the context is relevant return NO_INFO. 
        Remember, *DO NOT* edit the extracted parts of the context.
        Query: ${query}
        Answer:`;
		};
		// Create an instance of response synthesizer
		const responseSynthesizer = new ResponseSynthesizer({
			responseBuilder: new CompactAndRefine(undefined, newTextQaPrompt),
		});
		const index = await VectorStoreIndex.fromDocuments([document]);

		const queryEngine = index.asQueryEngine({ responseSynthesizer });

		const response = await queryEngine.query({
			query: query,
		});
		res.status(200).send(response.response);
	} catch (error) {
		console.error('Error in providing an answered with RAG: ', error);
		res.status(500).send('Failed to provide an answer with RAG');
	}
});

export default router;
