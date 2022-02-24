#!/bin/bash

bluetoothctl -- scan on
wait ${!}
exit
