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

### Install from PyPI
```sh
pipx install crllm
```

## 🌐 Configuration
CRLLM supports multiple backends for LLM code reviews. You can configure it by adding an configuration file `crllm_config.toml` in the root of your project. To initialize your project you can use

```bash
crllm -i .
```

This command guides you through the most important settings. You can find more information on the setting options in the [Wiki](https://github.com/lukasrump/crllm/wiki#-configuration).

## ✨Usage
CRLLM is designed to be easy to use right from your terminal. Below are some examples of how you can leverage the tool.

To perform a code review for a file or GIT repository run:
```sh
crllm path/to/your/codefile.py
```

### Enabling RAG Support

To enhance code reviews with source context, enable RAG (Retrieval-Augmented Generation) in `crllm_config.toml`:

```toml
[rag]
enabled = true
embedding_model = "all-minilm"      # Specify the embedding model
src_path = "./"                     # Define the root path of your source code
src_glob = "**/*.py"                # Use glob patterns to match source files (e.g., Python files)
```

### Ignore files
CRLLM supports a `.crllm_ignore` file to exclude specific files and directories from code reviews. This is similar to `.gitignore` but specific to CRLLM's code review process.