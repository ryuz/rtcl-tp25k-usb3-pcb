日本語版: [README.md](README.md)

# Original Base Board for Tang Primer 25K with FT601 + MIPI Connector

## Overview

The GW5A-LV25MG121 on the Sipeed [Tang Primer 25K](https://wiki.sipeed.com/hardware/en/tang/tang-primer-25k/primer-25k.html) includes a MIPI D-PHY interface, and the routing appears to reach the SoM. However, on the standard Dock base board, these lines are left unconnected and therefore cannot be used.

This project provides design data for an original base board for Tang Primer 25K that breaks out the MIPI D-PHY lines to a 0.5 mm pitch 22-pin connector and enables USB 3.0 connectivity via FT601 for exchanging image data and similar payloads with a PC.

## Schematic

The schematic is available here:

- [rtcl-tp25k-usb3_v1.pdf](rtcl-tp25k-usb3_v1.pdf)

## KiCad Design Data

KiCad 6.0 design data is stored under the rtcl-tp25k-usb3 directory.

## Disclaimer

This design data is provided for research and prototyping purposes. The author is not responsible for any damages arising from its use.

## License

This design data is provided under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You may freely use it for hobby or R&D purposes as long as you do not sell or distribute manufactured boards without authorization.

If you would like to manufacture and sell boards commercially, please contact the author separately for a commercial license agreement via the [contact form](https://rtc-lab.com/contact/).

## Author

Ryuji Fuchikami  
[Real-Time Computing Laboratory](https://rtc-lab.com/)
