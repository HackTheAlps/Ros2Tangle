# Streams Decoder
We used the Streams Decoder from [IOT2TANGLE repo](https://github.com/iot2tangle/streams-decoder) as an interface to get data from the IOTA tangle.
We changed the Streams Decoder code slightly as we faced following:
- the robot code part is sending the robot data as a valid JSON to the Streams Gateway. The streams decoder calls the IOTA tangle and gets valid JSON data. In the handlers.rs file, this data is modified slightly: the data part of the JSON contains "\". This invalid JSON is then returned as response by the REST API of the streams decoder.
- the robot is sending only the current state / joint_state message (status of the moment). The tangle returns the whole history of this device. We only want the so called delta (only the update) and not the whole history. As we are not yet experts in RUST and the IOTA tangle, we made here a quick fix in order to get only the newest data set.

PS: its the first time that we worked with the programming language Rust. Therefore, the code is not perfect, but it works in the way we require it. And hey, its a hackathon! So we hack ;-) (in this case)

## Usage
Download the Streams Decoder linked above and swap the _handlers.rs_ file with this one in this repo. Start the Streams decoder as described in the general description