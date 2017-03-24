# Aurora
Python interface for [Nanoleaf Aurora](https://nanoleaf.me/en/consumer-led-lighting/products/smarter-series/nanoleaf-aurora-smarter-kit/) lights. This is mostly hacking.

First, set the Aurora into pairing mode by holding the power button for 5 seconds. Then run:
```
python pairing.py
```
To get the token for your device. The token will land in a file `aurora.token`.
Now you can run:

```
python aurora.py
```
To connect to the device and switch it on and then off again.

More to come.

