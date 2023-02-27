General process:

* Find a model you are interested int
* Create a space. Make sure to specify a "Gradio Interace" when creaging the space
* Create a file called app.py
    * Copy/paste the code from the model's huggingface page
    * Write an inference function that makes an inference with model and input
    * Write a gradio interface that takes user input and calls inference function.
    * Create a requirements.txt file and add all required dependencies
* Commit changes or use online editor.
    * Huggingface space will automatically build on new changes
    * Monitor build log for any errors

