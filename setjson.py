{
  // 🧼 Tata letak & kenyamanan editor
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.rulers": [88],
  "editor.wordWrap": "on",
  "editor.lineNumbers": "on",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },

  // 🐍 Interpreter Python
  "python.defaultInterpreterPath": "${workspaceFolder}/env/bin/python",

  // 🧪 Linting & IntelliSense
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.analysis.typeCheckingMode": "basic",

  // 🧰 Jupyter (Notebook & Lab)
  "jupyter.sendSelectionToInteractiveWindow": true,
  "jupyter.interactiveWindowMode": "perFile",

  // 📦 Virtual environment auto-detection
  "python.venvPath": "${workspaceFolder}/env"
}
