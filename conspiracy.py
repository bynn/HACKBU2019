from textgenrnn import textgenrnn
import sys
import io

# textgen = textgenrnn()
# textgen.train_from_file('jokes.txt',num_epochs=20)



def jokes():
    textgen = textgenrnn('textgenrnn_weights.hdf5')
    old_stdout = sys.stdout # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    textgen.generate(temperature=0.9)
    sys.stdout = old_stdout # Put the old stream back in place
    whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
    return str(whatWasPrinted)
