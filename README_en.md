日本語版: [README.md](README.md)

# Original Base Board for Tang Primer 25K with FT601 + MIPI Connector

## Overview

The GW5A-LV25MG121 on the Sipeed [Tang Primer 25K](https://wiki.sipeed.com/hardware/en/tang/tang-primer-25k/primer-25k.html) includes a MIPI D-PHY interface, and the routing appears to reach the SoM. However, on the standard Dock base board, these lines are left unconnected and therefore cannot be used.

This project provides design data for an original base board for Tang Primer 25K that breaks out the MIPI D-PHY lines to a 0.5 mm pitch 22-pin connector and enables USB 3.0 connectivity via FT601 for exchanging image data and similar payloads with a PC.

![pcb_photo](doc/images/pcb_photo.png)

This board makes use of the MIPI pins that were originally unused on the Tang Primer 25K SoM. Even without leveraging MIPI, it can also be seen simply as a board that enables FPGA use over USB 3.0 — making it a great first step toward serious FPGA development for those who have previously been limited to UART-level connectivity between an FPGA and a PC.

Note: Although untested by the author, the MIPI D-PHY on the GW5A-LV25MG121 is bidirectional, so it may also be applicable to display-related experiments such as MIPI-DSI.


## Specs

Main features:

- Tang Primer 25K Core mounting connector
- USB 3.0 connectivity via FT601
- 4-lane MIPI connector (22-pin)
- One PMOD connector
- 4 LEDs
- 2 push switches
- 2-position DIP switch
- 6-pin header for JTAG

JTAG requires a separate external download cable. When using tools such as [openFPGALoader](https://github.com/trabucayre/openFPGALoader), a wide range of download cables are supported.

When using an FT232HL or similar, on-chip debugging via GOWIN EDA's GAO is also possible.


## System Images

### Camera Connection

Example connections with the [Raspberry Pi V2 Camera](https://www.raspberrypi.com/documentation/accessories/camera.html) and the author's own [RTCL-P3S7-MIPI](https://rtc-lab.com/products/rtcl-cam-p3s7-mipi/).

![Camera connection](doc/images/camera_photo.png)

### JTAG Connection

Example connections with the Digilent [JTAG-HS2](https://digilent.com/reference/programmers/jtag-hs2/start) and the Akizuki Denshi [FT232HL High-Speed USB Serial Conversion Module](https://akizukidenshi.com/catalog/g/g106503/).

![JTAG connection](doc/images/jtag_photo.png)


## Design Data

### Schematic

The schematic is available here:

- [rtcl-tp25k-usb3_v2.pdf](rtcl-tp25k-usb3_v2.pdf)

### KiCad Design Data

KiCad 10.0 design data is stored under the rtcl-tp25k-usb3 directory.

![design_image](doc/images/design_image.png)

Designed for manufacturing with JLCPCB's `JLC04161H-3313` stackup.


### Software

Currently under development at:

https://github.com/ryuz/rtcl-designs/tree/main/projects/rtcl_tp25k_usb3


## Disclaimer

This design data is provided for research and prototyping purposes. The author is not responsible for any damages arising from its use. No quality guarantee of any kind is provided for the design data.

## License

This design data is provided under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You may freely use it for hobby or R&D purposes as long as you do not sell or distribute manufactured boards without authorization.

If you would like to manufacture and sell boards commercially, please contact the author separately for a commercial license agreement via the [contact form](https://rtc-lab.com/contact/).

## Author

Ryuji Fuchikami  
[Real-Time Computing Laboratory](https://rtc-lab.com/)
