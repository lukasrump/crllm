# CRLLM

**Effortlessly Get Code Reviews from Large Language Models!**

CRLLM is a powerful command-line tool that enables developers to get code reviews from state-of-the-art Large Language Models (LLMs). Whether you want to use Ollama for locally running LLMs or connect to cloud services like ChatGPT, Hugging Face, and Azure, CRLLM has you covered. Improve your code quality, catch potential bugs, and receive AI-driven suggestions to enhance your development workflow. Get recommendations on best practices, bug-prone areas, and potential refactoring.
Learn from the suggestions how to improve your code, gaining new insights and techniques. Reduce the need for back-and-forth during human code reviews by catching more issues upfront.

## 🚀 Features

- **Flexible LLM Options**: Use Ollama to run models locally or leverage APIs from cloud providers like OpenAI, Hugging Face, and Azure.
- **Comprehensive Code Review**: Get quality feedback on code, including recommendations for readability, efficiency, and best practices.
- **Developer Productivity**: Integrate seamlessly into your existing development environment to speed up code review processes.
- **Privacy Control**: Choose between local or cloud-based solutions depending on your privacy needs and computational power.
- **Multi-Language Support**: Review code written in various programming languages (e.g., Python, JavaScript, Java, etc.).
- **Git Support**: Get Reviews for your Git changes or differences between branches.

## 🛠️ Installation

To get started with crllm, follow these simple installation steps:

### Prerequisites

- **Python 3.8+**: Make sure you have Python installed.
- **pipx**: https://pipx.pypa.io/stable/installation/
- **ollama**: https://ollama.com/download 
If you want to run the modells locally otherwise you will need the corresponding API keys for your provider



### Install from GitHub
```sh
pipx install git+https://github.com/lukasrump/crllm.git
```

## 🌐 Configuration
CRLLM supports multiple backends for LLM code reviews. You can configure it by adding an configuration file `crllm_config.toml` in the root of your project.

This TOML configuration file is splitted in four main sections:

### [project]
- **`description`**: Short project summary.

### [crllm]
- **`loader`**: Mechanism to load the source code, `"git"` by default.
- **`provider`**: LLM provider, `"ollama"`by default.
- **`git_main_branch`**: Specifies the main git branch, default is `"main"`.
- **`git_changed_lines`**: If `true`, only reviews changed lines.

#### Loaders
- **file**: Code review for a single source code file
- **git**: Reviews all changed files in the git repository
- **git_compare**: Reviews the difference between the current git branch and the `git_main_branch`

### [model]
The model settings depend on the provider. The model settings are the same as those of the [LangChain](https://python.langchain.com/docs/integrations/chat/) ChatModels. Per default crllm tries to use a locally installed ollama instance with llama3.1.

#### Ollama Local Setup
- **`model`**: Specifies the model to use, e.g `"llama3.1"`. Make sure that you pulled that model before you use it.

#### OpenAI API
- **`model`**: Specifies the model to use, e.g `"gpt-4o"`.

In addition you have to define the api key in your environment (`.env`)
```
OPENAI_API_KEY=your_openai_api_key
```
#### Hugging Face API
- **`repo_id`**: Specifies the repository to use, e.g `"HuggingFaceH4/zephyr-7b-beta"`.
- **`task`**: Specifies the task, e.g `"text-generation"`.

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

#### Azure OpenAI
- **`azure_deployment`**: Specifies the deployment to use, e.g `"gpt-35-turbo"`.
- **`api_version`**: Specifies the api version to use, e.g `"2023-06-01-preview"`.

In addition you have to define some variables in your environment (`.env`)

```
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com
```

### [prompt]
- **`template`**: Override the prompt template that is used (optional).

## ✨Usage
CRLLM is designed to be easy to use right from your terminal. Below are some examples of how you can leverage the tool.

To perform a code review for a file or GIT repository run:
```sh
crllm path/to/your/codefile.py
```