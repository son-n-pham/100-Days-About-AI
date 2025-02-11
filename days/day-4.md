## Day 4: VS Code Extension

### What is extension in VS Code?

It is add-on software that enhances the functionality of Visual Studio Code. It can be a new language support, debugging, or code snippets.

There are several extensions available in the marketplace, which can easily be installed in VS Code.

For AI assistant, I would suggest:

- Github Copilot: Provided by Microsoft, it is an AI pair programmer that helps you write code faster. It has free tier for light usage.
- Cline and Roo Code (prev. Roo Cline):
  - Both extensions are very similar as Cline is the pre-decessor of Roo Code
  - I am using both Cline and Roo Code, but prefer Roo Code more as it seems to be more stable for me
  - There are several free LLM APIs which we can use for personal projects. Currently, I mainly used models provided by VS Code LM API (Actually provided by Github Copilot). There are other free APIs available including Google Gemini, Codestral from Mistral and low cose DeepSeek.

### How to develop an extension?

I have used extensions for a while, but never thought of developing one until watching a 7-minute clip from Beyond Fireship.

https://www.youtube.com/watch?v=clJCDHml2cA&t=81s

The clip is informative and short (only 7 minutes); however, it was taking me about 3 hours to develop the extension similar to the clip. There are quite lots of learning I got from this experience.

- Step by step how to develop an VS Code extension by TypeScript
  - Thanks to AI assistant, the learning is quite smooth as I have a untired teacher who I can ask all types of silly questions. 🤣
  - Despite the usage of AI assistant, there are still lots of documentation reading in VS Code API in order to understand the structure of the extension.
- How to calling an local LLM provided by Ollama in an extension written by TypeScript

This is a baby step for a bigger one, which I can contribute to the open-source community to build more useful extensions for everyone and/or to inherit the existing extensions to customize for my own needs.

Here is the repo for this extension, and of course, it is open-source with MIT license. The extension is calling Ollama endpoint to use DeepSeek-R1-Distill-Qwen-7B model. I structured the repo in a way which I can easily review and remember the steps I have done for learning purpose. So please fee free to use it for your own learning.
https://github.com/son-n-pham/fireship-ext

### What's next?

The above extension is a simple chatbot with a local open-source LLM model. I have a quick discussion with one of my friends about safety with LLMs, and specifically about safety with DeepSeek model. Safety is a big topic, which I will have a quick personal thought on it on the next day.
