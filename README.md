# Reverse Mnist Network

I previously built an mnist handwritten digit classification project ([this repo](https://github.com/IAmDaanE/ai-digit-recognition)) and was wondering, cant i just completely reverse the neural network and the way values flow through it. The already give a bigger result for the wanted paths right? From now on the network's input nodes are scores from 0 to 1 for all 10 digits and the outputs are 784 pixel values.

<img width="1168" height="734" alt="Schermafbeelding 2026-10-31 232904" src="https://github.com/user-attachments/assets/9a9b6d87-7ce6-4795-9945-73d198b59263" />

## About the Project

To properly test this i made a UI where you can manually change the input score for each digit and then watch what the network makes of that. To attempt to make the results clearer i also did some color processing like boosting pixels that are closer to the center and making the colors exponentially increase in brightness instead of linearly. I will spoil that the results aren't great, forward passes with an activation function are lossy and pretrained models aren't meant to just be turned around, this project was a great excuse to built this [awesome pygame GUI library](https://github.com/IAmDaanE/skyline-pygame) called skyline though.

**Requires:** Python 3.10 - 3.14
1. Install the required libraries, preferably in a venv.

    ```
    pip install -r requirements.txt
    ```

2. Run the program.

    ```
    python src/inference_ui.py
    ```

## License

This project is open-source and available under the MIT License.
