import streamlit as st
import streamlit.components.v1 as components
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Streamaxpedia",
    page_icon="🤖",
    layout="wide", # Uses full width so the interactive web component can span perfectly
    initial_sidebar_state="collapsed"
)

# --- 1. PYTHON DATABASE PORT ---
TERMINOLOGY_DB = [
    # Hardware
    { 
        "term": "AD Plus 2.0", 
        "category": "DASHCAM", 
        "desc": "Streamax bread-and-butter 4-channel dashcam.", 
        "related": ["PBM", "ADAS", "PBP", "DSC", "DMS", "C29N"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=15UTpGJD4U4hPTktn3UjW-7xFUcD6X3PN" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1nGmQytGKRr288kGiqI4ci651liqmxKdx" }
        ] 
    },
    { 
        "term": "AD Max", 
        "category": "DASHCAM", 
        "desc": "Flagship 6-channel AI dashcam.", 
        "related": ["ADAS", "DSC", "DMS", "Black Light", "eSIM", "eMMC"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1nciNxEXenYg0qSWyGUdI0nnYVAZP7TPr" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1yGJIAe0S25mELDQfNx3dtBLNZ4ONXMkt" }
        ] 
    },
    { 
        "term": "C6 Lite 2.0", 
        "category": "DASHCAM", 
        "desc": "Economic, ADAS/DSC dashcam.", 
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1PC1fbWuVgPgWSEt3asOIKQA1JOtdE0fa" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1uYe7JIQffiepX3oIWi3sEImrlUYi3Sdd" }
        ] 
    },
    { 
        "term": "GT1 Pro", 
        "category": "GATEWAY", 
        "desc": "Telematics FMS gateway. (currently restricted to sell in USA)", 
        "related": ["DC Max"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1SPIEBvK1mvP3mMsJp36lRTZY-Ys88SBI" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1j6Bc6omBKMFRqb2IMGdJv-b6wIsYRumo" }
        ] 
    },
    { 
        "term": "DC Max", 
        "category": "DASHCAM", 
        "desc": "6-channel AI dashcam used with GT1 Pro. Cannot be individually deployed without GT1 Pro.", 
        "related": ["GT1 Pro"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=181wM9Jg9omsyzttMrHHNInshYjqAEqY-" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1eucgSJmlEsBC0tNPQ90aR_5s3dYJksk0" }
        ] 
    },
    { 
        "term": "PBM", 
        "category": "AD PLUS 2.0 ACCESSORIES", 
        "desc": "Power Box Max. It enables AD Plus 2.0 for additional 2-channel extension and CAN interpretation capability.",
        "related": ["AD Plus 2.0"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1dVh-YNKubqhr5mJMpaBhCfLoWVMrlKRy" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=12zNPRXFRAFqDuGEQLpw9rTBfbP4OraIo" },
            { "label": "Download PBM vs. PBP", "url": "https://drive.google.com/uc?export=download&id=1da0R5LaYIKJ4kX2EujskfY_JNVT_3-oW" }
        ]
    },
    { 
        "term": "PBP", 
        "category": "AD PLUS 2.0 ACCESSORIES", 
        "desc": "Power Box Plus. It enables CAN interpretation capability for AD Plus 2.0.", 
        "related": ["AD Plus 2.0", "PBM", "CAN Bus", "OBD-II"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1_mPVTAcyUx_0_ZjgJ11Zp5b2NVuHsSQc" },
            { "label": "Download PBM vs. PBP", "url": "https://drive.google.com/uc?export=download&id=1da0R5LaYIKJ4kX2EujskfY_JNVT_3-oW" }
        ] 
    },
    { 
        "term": "M1N 2.0", 
        "category": "MDVR", 
        "desc": "Bread-and-butter MDVR.", 
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1hlQ-5vNlxoZ7dH7I0L2uOY4bj3CX9ie5" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1Q7xYb6jG8E0ZHgWDDVuuWMI9w5vecmvA" }
        ] 
    },
    { 
        "term": "F6N", 
        "category": "MDVR", 
        "desc": "5-channel 1080P recording MDVR.", 
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=160vMHwSffxZWIu1D-iqfKWs3TlmPOy1h" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1jFIymbi1M39JC8vpPu-s5EYUgjuymEBG" }
        ] 
    },
    { 
        "term": "M3N", 
        "category": "MDVR", 
        "desc": "New MDVR.", 
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=14-vI6TLJrhNSys4qgnbhHOewU0iEWHOa" }
        ] 
    },
    { 
        "term": "C29N", 
        "category": "ACCESSORIES", 
        "desc": "DMS camera.", 
        "related": ["DMS"],
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1nzOhRlXB0C0e-LuOOoXvuBozJEhq2i6H" }
        ] 
    },
    { 
        "term": "B2", 
        "category": "ACCESSORIES", 
        "desc": "Exterior alarm.", 
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1UzGW4DsjBVkYf2VfAWHfX8ci-HInzAxI" }
        ] 
    },
    {
        "term": "DP7Q",
        "category": "VISIBILITY",
        "desc": "Visibility display monitor.",
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=T96bTI_SFVYPAwTKVd0Dddw1" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1PaCk1L9Mg5KXwRndPlRpJxgZ5W6jHDr8" }
        ]
    },
    {
        "term": "DP7Q-T",
        "category": "VISIBILITY",
        "desc": "Visibility display monitor.",
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1DqoHoy7iEjxkXYGEGvBOUq3uQut2G6LT" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=14G4hocFebDV14ltGeulSAFv8AzoVyJBC" }
        ]
    },
    {
        "term": "DP7Q-RT",
        "category": "VISIBILITY",
        "desc": "Visibility display monitor.",
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1tjEZOUmVAJHkl7uPvwtwv68ZEPeng_cj" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1Wiz44D3G8VkarQU3b-6ivcoABimu_k4u" }
        ]
    },
    {
        "term": "DP7S",
        "category": "VISIBILITY",
        "desc": "Visibility display monitor.",
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/uc?export=download&id=1rn0NpghwO0ls_diXBITzDLoRUh-YacSu" },
            { "label": "Download User Manual", "url": "https://drive.google.com/uc?export=download&id=1m9f5KCf4L8BGPIsE6VbzxEoBYdcJ8N59" }
        ]
    },
    {
        "term": "DP7S-T",
        "category": "VISIBILITY",
        "desc": "Visibility display monitor.",
        "files": [
            { "label": "Download Spec", "url": "https://drive.google.com/file/d/1AUd-_h-6YUheKkQy8IF" }
        ]
    },
    { 
        "term": "TF Card", 
        "category": "Hardware", 
        "desc": "TransFlash Card. A small flash memory card used for storing data, functionally identical to a microSD card, widely used in dashcams and other devices." 
    },
    { 
        "term": "NPU", 
        "category": "Hardware", 
        "desc": "Neural Processing Unit. A specialized processor designed to accelerate AI and machine learning tasks, especially those involving neural networks. Optimized for high-efficiency parallel computation." 
    },
    { 
        "term": "G-sensor", 
        "category": "Hardware", 
        "desc": "Accelerometer. A device measuring gravitational acceleration and motion forces. Detects changes in velocity, orientation, tilt, and impact to trigger event-based recording when sudden movements or collisions are detected." 
    },
    { 
        "term": "OBD Power Supply", 
        "category": "Hardware", 
        "desc": "Uses a vehicle’s standardized OBD-II port to provide electrical power (12V DC) to external devices. Allows for easy plug-and-play installations without hardwiring.", 
        "related": ["OBD-II"] 
    },
    { 
        "term": "Bus (in computing)", 
        "category": "Hardware", 
        "desc": "A communication system that transfers data between components inside a computer or between computers. It consists of a shared set of wires or paths through which data signals are sent." 
    },
    { 
        "term": "SoC", 
        "category": "Hardware", 
        "desc": "System on Chip. An integrated circuit that combines a processor, memory, input/output interfaces, and communication modules into a single chip, designed for efficient embedded computing in compact systems like telematics gateways." 
    },
    { 
        "term": "Gyroscope", 
        "category": "Hardware", 
        "desc": "A sensor measuring angular velocity or rotational motion around one or more axes. In telematics, it helps estimate orientation, steering behavior, and motion dynamics, often part of an IMU." 
    },
    { 
        "term": "Analog", 
        "category": "Hardware", 
        "desc": "A continuous signal representing physical measurements, varying smoothly over time (e.g., voltage, current, sound waves), as opposed to discrete digital signals." 
    },
    { 
        "term": "GPS Tracker", 
        "category": "Hardware", 
        "desc": "An electronic device that determines and communicates its geographic location using the Global Positioning System (GPS). Integrates GNSS receivers, cellular modems, IMUs, and vehicle interfaces (OBD-II, CAN) to collect and transmit location and telematics data." 
    },
    { 
        "term": "Telematics Gateway", 
        "category": "Hardware", 
        "desc": """A centralized embedded system installed in vehicles that aggregates, processes, and transmits data collected from onboard sources (CAN Bus, GPS, sensors) to external cloud platforms. Acts as the primary interface between in-vehicle electronics and remote data consumers.<br><br><b>Core Functions:</b><ul><li>Data aggregation from multiple networks.</li><li>Real-time processing of GPS and diagnostics.</li><li>Secure over-the-air (OTA) updates and edge computing.</li></ul><div class="diagram-box"><div class="diagram-title">Telematics Gateway Connections</div><div class="flex-col" style="gap:15px;"><div class="flow-gateway" style="width: 200px; letter-spacing: 1px;">TELEMATICS GATEWAY</div><div class="flex-row" style="gap:25px; align-items: flex-start;"><div class="flow-arrow"><div style="width:2px; height:20px; background:var(--text-grey); margin-bottom:5px;"></div><i class="fa-solid fa-plug" title="OBD/CAN Interface"></i><small>OBD/CAN</small></div><div class="flow-arrow"><div style="width:2px; height:20px; background:var(--text-grey); margin-bottom:5px;"></div><i class="fa-solid fa-satellite-dish" title="GPS/GNSS"></i><small>GPS</small></div><div class="flow-arrow"><div style="width:2px; height:20px; background:var(--text-grey); margin-bottom:5px;"></div><i class="fa-solid fa-car" title="Vehicle Sensors"></i><small>Sensors</small></div><div class="flow-arrow"><div style="width:2px; height:20px; background:var(--text-grey); margin-bottom:5px;"></div><i class="fa-solid fa-wifi" title="Wireless Comm"></i><small>Cellular</small></div></div></div></div>""",
        "related": ["GT1 Pro", "CAN Bus", "OBD-II"]
    },

    # Core Telematics
    { "term": "Telematics", "category": "Core Telematics", "desc": "The integrated use of telecommunications and informatics to monitor and manage vehicles remotely." },
    { "term": "CAN Bus", "category": "Core Telematics", "desc": """Controller Area Network. A robust, multi-master serial communication protocol designed to allow microcontrollers and Electronic Control Units (ECUs) to communicate without a host computer. Optimized for reliable real-time communication in electrically noisy environments.<br><br><b>Features:</b><ul><li><b>Classical CAN:</b> Up to 8 bytes payload.</li><li><b>CAN FD:</b> Up to 64 bytes payload.</li><li>Uses a differential two-wire topology (CAN_H and CAN_L).</li></ul><div class="diagram-box"><div class="diagram-title">CAN Message Frame</div><div class="flex-row" style="gap:2px;"><div class="frame-block bg-blue rounded-l" style="flex:1;">SOF<small>1 bit</small></div><div class="frame-block bg-orange" style="flex:2;">Identifier<small>11/29 bits</small></div><div class="frame-block bg-green" style="flex:1;">Control<small>6 bits</small></div><div class="frame-block bg-purple" style="flex:3;">Data<small>0-64 bytes</small></div><div class="frame-block bg-pink" style="flex:1;">ACK<small>2 bits</small></div><div class="frame-block bg-grey rounded-r" style="flex:1;">EOF<small>7 bits</small></div></div></div>""" },
    { "term": "OBD-II", "category": "Core Telematics", "desc": """On-Board Diagnostics II. A standardized automotive diagnostic system providing access to vehicle health and emissions-related information through a 16-pin Data Link Connector (DLC). Enables retrieval of Diagnostic Trouble Codes (DTCs), real-time sensor data, and system status.<br><br>Supports protocols like SAE J1850, ISO 9141-2, ISO 14230-4, and ISO 15765-4 (CAN).<div class="diagram-box"><div class="diagram-title">OBD-II Connector Pinout (Female)</div><div class="flex-col"><div class="flex-row"><div class="pin">1</div><div class="pin pin-green" title="J1850 Bus +">2</div><div class="pin">3</div><div class="pin pin-grey" title="Chassis Ground">4</div><div class="pin pin-grey" title="Signal Ground">5</div><div class="pin pin-blue" title="CAN High">6</div><div class="pin pin-orange" title="K-Line">7</div><div class="pin">8</div></div><div class="flex-row"><div class="pin">9</div><div class="pin pin-green" title="J1850 Bus -">10</div><div class="pin">11</div><div class="pin">12</div><div class="pin">13</div><div class="pin pin-blue" title="CAN Low">14</div><div class="pin pin-orange" title="L-Line">15</div><div class="pin pin-red" title="Battery +12V">16</div></div></div><div class="diagram-legend"><span class="c-grey">■ Ground (4,5)</span><span class="c-red">■ +12V Power (16)</span><span class="c-blue">■ CAN (6,14)</span><span class="c-orange">■ K-Line (7,15)</span></div></div>""" },
    { "term": "ECU", "category": "Core Telematics", "desc": "Electronic Control Unit. An embedded system in automotive or industrial equipment that manages a specific set of functions through real-time data processing and control. Each ECU contains a microcontroller or microprocessor, memory, and I/O interfaces connected to sensors and actuators." },
    { "term": "IVMS", "category": "Core Telematics", "desc": "In-Vehicle Monitoring System. A platform that records and analyzes driver and vehicle data for safety and efficiency management." },
    { "term": "Truck", "category": "Core Telematics", "desc": "Vehicles that carry cargo, materials, and non-human transportation." },
    { "term": "DTC", "category": "Core Telematics", "desc": "Diagnostic Trouble Code. A standardized code used by a vehicle’s onboard computer (ECU or ECM) to identify and report malfunctions or errors in the system.", "related": ["ECU"] },
    { "term": "SAE", "category": "Core Telematics", "desc": "Society of Automotive Engineers. A professional association and global standards organization for engineering professionals. Best known for developing and maintaining technical standards like the 'SAE J' series (e.g., J1939, J1708) ensuring safety and interoperability." },
    { "term": "J1939", "category": "Core Telematics", "desc": """SAE J1939 Protocol. A high-level communication protocol built on CAN Bus, specifically designed for heavy-duty commercial vehicles. It standardizes messages exchanged between ECUs and defines parameters for diagnostics, performance monitoring, and control.<br><br><b>Features:</b><ul><li>Uses 29-bit extended CAN identifiers.</li><li>Employs Parameter Group Numbers (PGNs) and Suspect Parameter Numbers (SPNs).</li><li>Supports both broadcast and peer-to-peer communication.</li></ul><div class="diagram-box"><div class="diagram-title">J1939 29-Bit Identifier Structure</div><div class="flex-row" style="gap:2px;"><div class="frame-block bg-orange rounded-l" style="flex:1;">Priority<small>3 bits</small></div><div class="frame-block bg-grey" style="flex:1;">Res<small>1 bit</small></div><div class="frame-block bg-blue" style="flex:2;">PDU Format<small>8 bits</small></div><div class="frame-block bg-green" style="flex:2;">PDU Specific<small>8 bits</small></div><div class="frame-block bg-purple rounded-r" style="flex:2;">Source Addr<small>8 bits</small></div></div></div>""", "related": ["CAN Bus", "FMS", "SAE"] },
    { "term": "FMS", "category": "Core Telematics", "desc": """Fleet Management System Protocol. A standardized, manufacturer-endorsed data interface derived from SAE J1939. It allows third-party telematics providers secure, read-only access to selected vehicle operational data (e.g., fuel consumption, engine speed) without compromising vehicle control logic.<div class="diagram-box"><div class="diagram-title">FMS Technical Architecture</div><div class="flex-row" style="gap:15px;"><div class="flex-col" style="gap:8px;"><div class="flow-node">ECU</div><div class="flow-node">ECU</div></div><div class="flow-arrow"><i class="fa-solid fa-arrow-right-long"></i><small>CAN Bus</small></div><div class="flow-gateway">FMS Gateway</div><div class="flow-arrow"><i class="fa-solid fa-cloud-arrow-up"></i><small>Cellular</small></div><div class="flow-cloud"><i class="fa-solid fa-cloud"></i></div></div></div>""", "related": ["J1939"] },
    { "term": "J1708", "category": "Core Telematics", "desc": """SAE J1708. A legacy serial communication protocol for heavy-duty vehicle networks, defining physical and data link layers for asynchronous communication over a shared twisted-pair bus. Largely succeeded by J1939.<div class="diagram-box"><div class="diagram-title">J1708 Message Structure</div><div class="flex-row" style="gap:2px;"><div class="frame-block bg-orange rounded-l" style="flex:1;">MID<small>1 byte</small></div><div class="frame-block bg-blue" style="flex:4;">Data<small>0-255 bytes</small></div><div class="frame-block bg-red rounded-r" style="flex:1;">Checksum<small>1 byte</small></div></div></div>""", "related": ["SAE"] },
    { "term": "K-Line", "category": "Core Telematics", "desc": "ISO 9141 / ISO 14230. A single-wire serial communication protocol primarily used in automotive diagnostics before CAN became dominant. Enables communication between diagnostic tools and ECUs." },
    { "term": "Dead Reckoning GPS", "category": "Core Telematics", "desc": "A hybrid localization technique estimating a vehicle’s position by combining inertial sensor data (IMU, wheel speed) with GPS inputs. Enables continuous tracking in environments where GPS signals are degraded (e.g., tunnels, urban canyons).", "related": ["GPS Tracker", "Kalman Filter"] },
    { "term": "RTK", "category": "Core Telematics", "desc": "Real-Time Kinematic. A satellite navigation technique enhancing GPS precision using real-time correction data from a nearby reference station, enabling centimeter-level positioning." },
    
    # AI Vision & Safety
    { "term": "ADAS", "category": "AI Vision & Safety", "desc": "Advanced Driver Assistance Systems. Electronic systems in vehicles that assist the driver in driving and parking functions. Using sensors, cameras, and AI, ADAS features such as lane keeping, collision warning, and adaptive cruise control enhance safety and reduce the risk of accidents.", "related": ["FCW", "LDW", "HMW", "PCW"] },
    { "term": "DMS", "category": "AI Vision & Safety", "desc": "Driver Monitoring System. An in-vehicle safety technology that uses cameras and sensors to monitor the driver's attentiveness, alertness, and behavior in real time. It detects signs of drowsiness, distraction, or inattention, and provides alerts or triggers safety interventions to prevent accidents.", "file": "https://drive.google.com/uc?export=download&id=1IVgGsg-SjJLDxpfiRjExRKmSDKdZZLPQ" },
    { "term": "DSC", "category": "AI Vision & Safety", "desc": "Driver Status Monitoring / Driver State Camera. A system that observes the driver's face and behavior to detect fatigue, distraction, or inattention. It uses infrared or RGB cameras with AI algorithms to issue warnings or take preventive action if necessary.", "file": "https://drive.google.com/uc?export=download&id=1IVgGsg-SjJLDxpfiRjExRKmSDKdZZLPQ" },
    { "term": "BSD", "category": "AI Vision & Safety", "desc": "Blind Spot Detection. Alerts drivers to vehicles or objects in their blind spots to prevent lane-change collisions." },
    { "term": "AVM", "category": "AI Vision & Safety", "desc": "Around View Monitoring. A driver-assistance system that uses multiple cameras around the vehicle to create a 360-degree bird’s-eye view. It enhances driver visibility for parking and low-speed maneuvers by displaying the vehicle’s surroundings in real time." },
    { "term": "AI", "category": "AI Vision & Safety", "desc": "Artificial Intelligence. Machine learning algorithms that analyze patterns in visual and telematics data to generate actionable insights." },
    { "term": "FCW", "category": "AI Vision & Safety", "desc": "Forward Collision Warning. An ADAS feature that detects the risk of a frontal collision using sensors such as radar or cameras. It alerts the driver when the vehicle is approaching another object too quickly.", "related": ["ADAS"] },
    { "term": "LDW", "category": "AI Vision & Safety", "desc": "Lane Departure Warning. A safety system that monitors the vehicle's position within lane markings. If the vehicle unintentionally drifts out of its lane without signaling, the system alerts the driver.", "related": ["ADAS"] },
    { "term": "HMW", "category": "AI Vision & Safety", "desc": "Headway Monitoring Warning. Measures the time or distance gap between the host vehicle and the vehicle in front, issuing a warning if the following distance becomes dangerously short.", "related": ["ADAS"] },
    { "term": "PCW", "category": "AI Vision & Safety", "desc": "Pedestrian Collision Warning. Detects pedestrians in or near the vehicle's path using forward-facing cameras and algorithms to alert the driver of a potential collision risk.", "related": ["ADAS"] },
    { "term": "MOIS", "category": "AI Vision & Safety", "desc": "Moving Off Information System. An advanced driver-assistance feature designed to detect vulnerable road users (VRUs), such as pedestrians and cyclists, in the immediate front area of a commercial vehicle when starting to move.", "related": ["ADAS"] },
    { "term": "AEBS", "category": "AI Vision & Safety", "desc": "Advanced Emergency Braking System. A vehicle safety system that automatically detects an imminent collision and applies the brakes to prevent or reduce severity.", "related": ["ADAS"] },
    { "term": "ACC", "category": "AI Vision & Safety", "desc": "Adaptive Cruise Control. Automatically adjusts the vehicle’s speed to maintain a safe following distance from the vehicle ahead, extending traditional cruise control using radar and cameras.", "related": ["ADAS"] },
    
    # Connectivity
    { "term": "MDVR", "category": "Connectivity", "desc": "Mobile Digital Video Recorder. A ruggedized video recording device designed specifically for use in vehicles (buses, trucks, taxis). Records and manages video input from onboard cameras, built to withstand mobile environments. Often includes GPS, 4G/5G, and ADAS/DMS integration." },
    { "term": "NVR", "category": "Connectivity", "desc": "Network Video Recorder. A network-based video storage device, often used in fixed installations." },
    { "term": "LTE / 4G / 5G", "category": "Connectivity", "desc": "Cellular network standards used for real-time data transmission and cloud connectivity." },
    { "term": "eSIM", "category": "Connectivity", "desc": "Embedded SIM. A programmable SIM card soldered into the device, enabling remote carrier management and connectivity." },
    { "term": "OTA", "category": "Connectivity", "desc": "Over-the-Air Update. Remote software update capability for hardware devices, improving maintainability and reducing service costs." },
    { "term": "API", "category": "Connectivity", "desc": "Application Programming Interface. A set of functions and protocols allowing systems to communicate and exchange data." },
    { "term": "GMSL", "category": "Connectivity", "desc": "Gigabit Multimedia Serial Link. A high-speed data transmission technology used in automotive applications to transmit video, audio, control signals, and power over a single cable." },
    { "term": "AHD", "category": "Connectivity", "desc": "Analog High Definition. A video surveillance standard that transmits high-definition video signals over coaxial cables using analog technology." },
    { "term": "IPC", "category": "Connectivity", "desc": "Internet Protocol Camera video output. Digital video signal generated over a network, requiring an NVR, computer, or software to view or record the stream." },
    { "term": "TCP", "category": "Connectivity", "desc": "Transmission Control Protocol. A core communication protocol that provides reliable, ordered, and error-checked delivery of data between applications over a network." },
    { "term": "NTP", "category": "Connectivity", "desc": "Network Time Protocol. Used to synchronize the clocks of computer systems over data networks to ensure all connected devices maintain consistent and accurate time." },
    { "term": "Broadcast Communication", "category": "Connectivity", "desc": "A network communication method where a single sender transmits a message received by all nodes simultaneously. Used in CAN and J1939 for periodic data updates (e.g., engine RPM) without needing a specific request." },
    { "term": "Peer-to-Peer Communication", "category": "Connectivity", "desc": "A targeted communication method where a sender transmits data specifically addressed to a single recipient node. Commonly used in diagnostics, configuration, or transport protocols (e.g., J1939 request/response)." },
    { "term": "RTOS", "category": "Connectivity", "desc": "Real-Time Operating System. An OS optimized for deterministic task execution, enabling time-sensitive functions such as vehicle diagnostics, data acquisition, and wireless communication." },
    
    # Data, Compliance & Metrics
    { "term": "FTP", "category": "Data & Metrics", "desc": "File Transfer Protocol. A standard network protocol used to transfer video files or logs from devices to servers." },
    { "term": "SDK", "category": "Data & Metrics", "desc": "Software Development Kit. A package of development tools allowing integration of Streamax systems with third-party platforms." },
    { "term": "FCC", "category": "Compliance", "desc": "Federal Communications Commission. U.S. certification body regulating electronic devices and communication standards." },
    { "term": "CE / E-mark", "category": "Compliance", "desc": "Certification marks indicating compliance with EU safety, health, environmental protection, and automotive component standards." },
    { "term": "GDPR", "category": "Compliance", "desc": "General Data Protection Regulation. European privacy regulation affecting data collection and processing from drivers and vehicles." },
    { "term": "ELD", "category": "Compliance", "desc": "Electronic Logging Device. A digital recorder installed in commercial motor vehicles to automatically log a driver’s Hours of Service (HOS). It tracks engine usage, vehicle movement, and driver identity to ensure compliance with FMCSA regulations.<br><br>Interfaces directly with the vehicle's electronic control systems via CAN Bus (J1939) or OBD-II port. Replaces traditional paper logbooks." },
    { "term": "Tachograph Systems", "category": "Compliance", "desc": "Devices installed in commercial vehicles to record key information about operation and driver activity (driving time, speed, rest periods). Mandated in the EU to ensure fair competition and road safety." },
    { "term": "MPG", "category": "Data & Metrics", "desc": "Miles Per Gallon. A measure of vehicle fuel efficiency." },
    { "term": "MTBF", "category": "Data & Metrics", "desc": "Mean Time Between Failures. A reliability metric describing the expected operational lifespan of a device." },
    { "term": "ROI", "category": "Data & Metrics", "desc": "Return on Investment. A key performance indicator measuring financial benefit relative to cost." },
    { "term": "TCO", "category": "Data & Metrics", "desc": "Total Cost of Ownership. The full cost of deploying and maintaining a system over its lifecycle." },
    { "term": "PID", "category": "Data & Metrics", "desc": "Proportional–Integral–Derivative. A widely used feedback control algorithm in engineering and automation that continuously calculates an error value and applies corrections to keep a variable close to a desired setpoint." },
    { "term": "Fleet Analytics", "category": "Data & Metrics", "desc": "The integration and analysis of data from GPS, J1939, OBD-II, and behavioral sensors to generate actionable intelligence. Used to track fuel consumption, optimize routing, perform predictive maintenance, and evaluate driver behavior." },
    { "term": "Vehicle Health Monitoring", "category": "Data & Metrics", "desc": "Continuous tracking and evaluation of a vehicle’s operational status using diagnostic and real-time data. Uses DTCs and SPNs to interpret faults, enabling proactive servicing and predictive diagnostics." },
    { "term": "Kalman Filter", "category": "Data & Metrics", "desc": "An algorithm that estimates the internal state of a linear dynamic system from a series of noisy measurements. Widely used in telematics to smooth GPS trajectories, fuse sensor data, and precisely estimate vehicle position and velocity.", "related": ["Dead Reckoning GPS"] },
    
    # Team
    { "term": "Jerry Li", "category": "TEAM", "desc": "Jerry Li，6爷，产品市场总监", "exact": True },
    { "term": "Ryan He", "category": "TEAM", "desc": "堃哥，全国熬夜加班总冠军，货运产品线总监。<br><br>名言：“干就完了！”", "related": ["Jerry Li"], "exact": True },
    { "term": "Jack Yi", "category": "TEAM", "desc": "不正经程序员，理工科市场推广员，PPT做的贼烂销售员", "related": ["Jerry Li"], "exact": True }
]

# Process Bidirectional Links Programmatically
for item in TERMINOLOGY_DB:
    if "related" in item:
        for related_term in item["related"]:
            target = next((t for t in TERMINOLOGY_DB if t["term"] == related_term), None)
            if target:
                if "related" not in target:
                    target["related"] = []
                if item["term"] not in target["related"]:
                    target["related"].append(item["term"])

# --- 2. STREAMLIT GLOBAL CSS ---
# This hides standard padding so our interactive HTML component can take the full screen
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe {
    border: none;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


# --- 3. FULL NATIVE WEB COMPONENT STRING ---
# Everything visual (Search bar, Keystroke engine, Mascot, Graph Modal) is placed 
# into this single HTML payload. This completely resolves the "Enter Key" limitation 
# of Streamlit and allows seamless instant interactions.

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Streamaxpedia Embedded</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --bg-deep: #050810;
            --bg-gradient: radial-gradient(circle at 50% -20%, #0B1221, #050810);
            --primary-green: #2AF598;
            --secondary-blue: #009EFD;
            --text-white: #FFFFFF;
            --text-grey: #A0AEC0;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: 1px solid rgba(255, 255, 255, 0.08);
            --card-radius: 12px;
            --font-main: 'Inter', sans-serif;
            --gradient-text: linear-gradient(135deg, var(--primary-green) 0%, var(--secondary-blue) 100%);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        body {
            background-color: var(--bg-deep);
            background-image: var(--bg-gradient);
            font-family: var(--font-main);
            color: var(--text-white);
            margin: 0; padding: 0;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* --- SEARCH CONTAINER --- */
        .search-wrapper { width: 100%; max-width: 800px; padding: 40px 20px; margin-top: 5vh; display: flex; flex-direction: column; align-items: center; transition: margin-top 0.5s ease; }
        .search-wrapper.active-search { margin-top: 1vh; }

        .title-container { display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 30px; }
        .subtitle-box { text-align: center; margin-top: -15px; margin-bottom: 30px; padding: 0 20px; }
        .temp-note { color: var(--text-grey); font-size: 0.95rem; font-style: italic; margin-bottom: 5px; }
        .credit-line { color: var(--primary-green); font-size: 0.85rem; font-weight: 600; margin-top: 0; letter-spacing: 0.5px; }

        /* --- MASCOT --- */
        .mascot-container { width: 140px; height: 140px; animation: float 4s ease-in-out infinite; perspective: 600px; z-index: 10; filter: drop-shadow(0 15px 20px rgba(42, 245, 152, 0.15)); }
        .mascot { width: 100%; height: 100%; object-fit: contain; transition: transform 0.15s ease-out; transform-origin: center center; }
        .mascot.jumping-heart { animation: heartBounce 0.4s infinite alternate cubic-bezier(0.5, 0.05, 1, 0.5); filter: none;}

        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-12px); } }
        @keyframes heartBounce { 0% { transform: translateY(0) scale(1); } 100% { transform: translateY(-20px) scale(1.15); } }

        .brand-title { font-size: 3rem; font-weight: 700; text-align: center; letter-spacing: -1px; margin: 0; }
        .gradient-text { background: var(--gradient-text); -webkit-background-clip: text; background-clip: text; color: transparent; }

        .search-box { width: 100%; position: relative; display: flex; align-items: center; }
        .search-input { width: 100%; padding: 20px 25px 20px 60px; font-size: 1.2rem; border-radius: 50px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); color: var(--text-white); font-family: var(--font-main); backdrop-filter: blur(10px); transition: var(--transition); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); }
        .search-input:focus { outline: none; border-color: var(--primary-green); background: rgba(255, 255, 255, 0.08); box-shadow: 0 0 20px rgba(42, 245, 152, 0.2); }
        .search-icon { position: absolute; left: 25px; font-size: 1.2rem; color: var(--text-grey); transition: var(--transition); }
        .search-input:focus ~ .search-icon { color: var(--primary-green); }
        .clear-icon { position: absolute; right: 25px; font-size: 1.2rem; color: var(--text-grey); cursor: pointer; display: none; transition: var(--transition); }
        .clear-icon:hover { color: var(--text-white); }

        .stats { width: 100%; max-width: 800px; margin: 0 auto 15px auto; padding: 0 20px; color: var(--text-grey); font-size: 0.9rem; display: none; }
        .stats.show { display: block; }
        .stats span { color: var(--primary-green); font-weight: bold; }

        /* --- RESULTS AREA --- */
        .results-container { width: 100%; max-width: 800px; padding: 0 20px 40px; display: flex; flex-direction: column; gap: 16px; }
        .result-card { background: var(--glass-bg); border: var(--glass-border); border-radius: var(--card-radius); padding: 24px; transition: var(--transition); opacity: 0; transform: translateY(10px); animation: fadeUp 0.3s forwards ease-out; position: relative; overflow: hidden; }
        .result-card::before { content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px; background: var(--gradient-text); opacity: 0.7; }
        .result-card:hover { background: rgba(255, 255, 255, 0.06); border-color: rgba(42, 245, 152, 0.3); transform: translateY(-2px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }
        @keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }

        .term-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
        .term-title { font-size: 1.4rem; font-weight: 700; color: var(--primary-green); margin:0; }
        .term-category { font-size: 0.75rem; text-transform: uppercase; background: rgba(0, 158, 253, 0.1); color: var(--secondary-blue); padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(0, 158, 253, 0.3); }
        .term-desc { font-size: 1rem; color: var(--text-grey); line-height: 1.6; margin-bottom: 10px; }
        .highlight { background: rgba(42, 245, 152, 0.2); color: #2AF598; padding: 2px 4px; border-radius: 4px; }

        .download-btn, .relevance-btn { display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; border-radius: 20px; text-decoration: none; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: none; transition: var(--transition); }
        .download-btn { background: rgba(42, 245, 152, 0.1); color: var(--primary-green); border: 1px solid var(--primary-green); margin-top: 12px; margin-right: 10px; }
        .download-btn:hover { background: var(--primary-green); color: var(--bg-deep); box-shadow: 0 0 15px rgba(42, 245, 152, 0.4); }
        .relevance-btn { background: rgba(0, 158, 253, 0.1); color: var(--secondary-blue); border: 1px solid var(--secondary-blue); }
        .relevance-btn:hover { background: var(--secondary-blue); color: var(--text-white); box-shadow: 0 0 15px rgba(0, 158, 253, 0.4); }

        /* --- DIAGRAMS --- */
        .diagram-box { margin-top: 15px; padding: 15px; background: rgba(0,0,0,0.3); border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); }
        .diagram-title { text-align: center; font-weight: 700; margin-bottom: 15px; color: var(--primary-green); font-size: 0.9rem; }
        .flex-row { display: flex; align-items: center; justify-content: center; gap: 5px; }
        .flex-col { display: flex; flex-direction: column; align-items: center; gap: 5px; }
        .frame-block { padding: 8px 4px; text-align: center; font-size: 0.75rem; color: #fff; display: flex; flex-direction: column; justify-content: center; }
        .frame-block small { opacity: 0.8; font-size: 0.65rem; margin-top: 3px; }
        .bg-blue { background: #3b82f6; } .bg-orange { background: #f59e0b; } .bg-green { background: #10b981; } .bg-purple { background: #8b5cf6; } .bg-pink { background: #ec4899; } .bg-grey { background: #64748b; } .bg-red { background: #ef4444; }
        .rounded-l { border-radius: 4px 0 0 4px; } .rounded-r { border-radius: 0 4px 4px 0; }
        .pin { width: 32px; height: 32px; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; border-radius: 4px; font-family: monospace; font-size: 0.8rem; color: rgba(255,255,255,0.5); }
        .pin-green { border-color: #10b981; color: #10b981; font-weight: bold; background: rgba(16,185,129,0.1); }
        .pin-grey { border-color: #a8a29e; color: #a8a29e; font-weight: bold; background: rgba(168,162,158,0.1); }
        .pin-blue { border-color: #3b82f6; color: #3b82f6; font-weight: bold; background: rgba(59,130,246,0.1); }
        .pin-orange { border-color: #f59e0b; color: #f59e0b; font-weight: bold; background: rgba(245,158,11,0.1); }
        .pin-red { border-color: #ef4444; color: #ef4444; font-weight: bold; background: rgba(239,68,68,0.1); }
        .diagram-legend { display: flex; justify-content: center; gap: 15px; margin-top: 15px; font-size: 0.75rem; flex-wrap: wrap; }
        .diagram-legend span { display: flex; align-items: center; gap: 4px; }
        .c-green { color: #10b981; } .c-grey { color: #a8a29e; } .c-blue { color: #3b82f6; } .c-orange { color: #f59e0b; } .c-red { color: #ef4444; }
        .flow-node { background: #10b981; color: #fff; padding: 6px 12px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
        .flow-gateway { background: #3b82f6; color: #fff; padding: 15px 10px; border-radius: 8px; font-weight: bold; font-size: 0.9rem; text-align: center; box-shadow: 0 4px 15px rgba(59,130,246,0.3); }
        .flow-cloud { background: #8b5cf6; color: #fff; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 4px 15px rgba(139,92,246,0.3); }
        .flow-arrow { color: var(--text-grey); display: flex; flex-direction: column; align-items: center; font-size: 1rem; }
        .flow-arrow small { font-size: 0.65rem; margin-top: 4px; }

        /* --- GRAPH MODAL --- */
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(5, 8, 16, 0.85); backdrop-filter: blur(8px); z-index: 1000; display: flex; justify-content: center; align-items: center; opacity: 0; visibility: hidden; transition: var(--transition); }
        .modal-overlay.active { opacity: 1; visibility: visible; }
        .modal-box { background: var(--glass-bg); border: var(--glass-border); border-radius: var(--card-radius); width: 95vw; height: 90vh; position: relative; padding: 20px; display: flex; flex-direction: column; align-items: center; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
        .close-modal { position: absolute; top: 20px; right: 20px; background: transparent; border: none; color: var(--text-grey); font-size: 1.5rem; cursor: pointer; z-index: 100; transition: var(--transition); }
        .close-modal:hover { color: var(--text-white); }
        
        .graph-viewport { width: 100%; flex: 1; position: relative; overflow: hidden; cursor: grab; background: rgba(0, 0, 0, 0.2); border-radius: 12px; margin-top: 10px; border: 1px solid rgba(255, 255, 255, 0.05); }
        .graph-viewport:active { cursor: grabbing; }
        .graph-container { position: absolute; top: 0; left: 0; display: flex; align-items: center; gap: 120px; padding: 100px; transform-origin: 0 0; will-change: transform; }
        .graph-col { display: flex; flex-direction: column; gap: 20px; position: relative; z-index: 2; }
        
        /* TABLET NODE STYLING UPDATE */
        .round-node { 
            background: rgba(255, 255, 255, 0.05); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            color: var(--text-white); 
            padding: 10px 20px; 
            border-radius: 20px; 
            min-width: 80px; 
            max-width: 160px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-weight: 600; 
            text-align: center; 
            backdrop-filter: blur(10px); 
            cursor: pointer; 
            position: relative; 
            z-index: 2; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.2); 
            font-size: 0.85rem; 
            line-height: 1.3; 
            white-space: normal;
            transition: var(--transition);
        }
        .node-master { 
            background: rgba(42, 245, 152, 0.1); 
            border-color: var(--primary-green); 
            color: var(--primary-green); 
            padding: 15px 30px; 
            border-radius: 25px; 
            font-size: 1.1rem; 
            min-width: 120px; 
            box-shadow: 0 0 20px rgba(42, 245, 152, 0.2); 
            cursor: default; 
        }
        .node-related:hover { background: var(--secondary-blue); color: var(--text-white); box-shadow: 0 0 20px rgba(0, 158, 253, 0.4); transform: scale(1.05); }
        .node-dist2 { margin-left: 100px; transform: scale(0.9); opacity: 0.9; }
        .node-dist2:hover { transform: scale(0.95); }
        
        .graph-lines { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; overflow: visible; }
        
        #modalChildExplanation { position: absolute; bottom: 20px; left: 20px; width: 350px; z-index: 100; box-shadow: 0 10px 30px rgba(0,0,0,0.5); background: rgba(5, 8, 16, 0.95); border: 1px solid var(--secondary-blue); padding: 16px 20px; border-radius: 8px; display: none; animation: fadeUp 0.3s ease-out forwards; }
        #modalChildExplanation.active { display: block; }
        .see-details-btn { background: var(--secondary-blue); color: #fff; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-weight: 600; font-size: 0.85rem; margin-top: 15px; display: flex; align-items: center; gap: 8px; transition: var(--transition); }
        .see-details-btn:hover { background: var(--primary-green); color: var(--bg-deep); }
    </style>
</head>
<body>

    <div class="search-wrapper" id="searchWrapper">
        <div class="title-container">
            <div class="mascot-container">
                <img src="https://drive.google.com/thumbnail?id=1bXf5psHrw4LOk0oMAkTJRL15_mLCabad&sz=w500" alt="Streamax Mascot" class="mascot" id="mascotImage" onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
            </div>
            <h1 class="brand-title"><span class="gradient-text">Streamaxpedia</span></h1>
        </div>
        
        <div class="subtitle-box">
            <p class="temp-note">
                <i class="fa-solid fa-circle-info" style="color: var(--secondary-blue); margin-right: 5px;"></i>
                This is a temporary Streamax info library. A more powerful Streamax AI agent is coming soon!
            </p>
            <p class="credit-line">
                <i class="fa-solid fa-bolt" style="margin-right: 5px;"></i>By Trucking BU - a Sales Toolkit Extension
            </p>
        </div>
        
        <div class="search-box">
            <!-- Native instant search keystroke input -->
            <input type="text" id="searchInput" class="search-input" placeholder="Search for ADAS, MDVR, APIs, metrics..." autocomplete="off" autofocus>
            <i class="fa-solid fa-magnifying-glass search-icon"></i>
            <i class="fa-solid fa-xmark clear-icon" id="clearBtn"></i>
        </div>
    </div>

    <div class="stats" id="statsBar">Found <span id="resultCount">0</span> terms</div>
    <div class="results-container" id="resultsContainer">
        <!-- Results will be injected here via JavaScript instantly without reloading -->
    </div>

    <!-- RELEVANCE GRAPH MODAL -->
    <div class="modal-overlay" id="relevanceModal">
        <div class="modal-box">
            <button class="close-modal" onclick="closeModal()"><i class="fa-solid fa-xmark"></i></button>
            <h3 style="color: var(--text-white); font-size: 1.2rem; margin-bottom: 5px; z-index: 10;">Relevance Graph</h3>
            
            <div class="graph-viewport" id="graphViewport">
                <div class="graph-container" id="graphContainer">
                    <svg class="graph-lines" id="graphLines" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"></svg>
                    <div class="round-node node-master" id="graphMasterNode"></div>
                    <div class="graph-col" id="graphRelatedNodes"></div>
                </div>
                <div id="modalChildExplanation"></div>
            </div>
        </div>
    </div>

    <script>
        // Load the Python database into JavaScript
        const terminologyDB = """ + json.dumps(TERMINOLOGY_DB) + """;
        
        let currentMascotSrc = 'https://drive.google.com/thumbnail?id=1bXf5psHrw4LOk0oMAkTJRL15_mLCabad&sz=w500'; 
        let isGraphDragging = false, graphStartX = 0, graphStartY = 0, graphTranslateX = 0, graphTranslateY = 0, hasGraphDragged = false;

        const searchInput = document.getElementById('searchInput');
        const resultsContainer = document.getElementById('resultsContainer');
        const searchWrapper = document.getElementById('searchWrapper');
        const clearBtn = document.getElementById('clearBtn');
        const statsBar = document.getElementById('statsBar');
        const resultCount = document.getElementById('resultCount');

        function escapeRegExp(string) { return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\$&'); }
        
        function highlightText(text, query) {
            if (!text) return '';
            if (!query) return text;
            const escapedQuery = escapeRegExp(query);
            const regex = new RegExp(`(${escapedQuery})(?![^<]*>)`, 'gi');
            return text.replace(regex, '<span class="highlight">$1</span>');
        }

        // --- SEARCH ENGINE LOGIC ---
        function performSearch() {
            const rawQuery = searchInput.value.trim();
            const query = rawQuery.toLowerCase();
            
            if (query.length > 0) {
                searchWrapper.classList.add('active-search');
                clearBtn.style.display = 'block';
            } else {
                searchWrapper.classList.remove('active-search');
                clearBtn.style.display = 'none';
                resultsContainer.innerHTML = '';
                statsBar.classList.remove('show');
                document.getElementById('mascotImage').src = currentMascotSrc;
                document.getElementById('mascotImage').classList.remove('jumping-heart');
                return;
            }

            const isExactMatch = terminologyDB.some(item => item.exact && item.term.toLowerCase() === rawQuery.toLowerCase());
            const mascotImg = document.getElementById('mascotImage');
            if (isExactMatch) {
                mascotImg.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23ff3366"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
                mascotImg.classList.add('jumping-heart');
            } else {
                mascotImg.src = currentMascotSrc;
                mascotImg.classList.remove('jumping-heart');
            }

            const scoredResults = terminologyDB.map(item => {
                let score = 0;
                if (item.exact) {
                    if (item.term.toLowerCase() === rawQuery.toLowerCase()) score += 1000;
                } else {
                    const lowerTerm = item.term.toLowerCase();
                    const lowerDesc = item.desc.toLowerCase();
                    const lowerCat = item.category ? item.category.toLowerCase() : '';
                    if (lowerTerm === query) score += 1000;
                    else if (lowerTerm.includes(query)) score += 500;
                    if (item.related && item.related.some(r => r.toLowerCase() === query)) score += 400;
                    else if (item.related && item.related.some(r => r.toLowerCase().includes(query))) score += 300;
                    if (lowerCat === query) score += 50;
                    else if (lowerCat.includes(query)) score += 20;
                    if (lowerDesc.includes(query)) score += 10;
                }
                return { item, score };
            }).filter(scoredItem => scoredItem.score > 0);

            scoredResults.sort((a, b) => b.score - a.score);
            const results = scoredResults.map(s => s.item);

            statsBar.classList.add('show');
            resultCount.textContent = results.length;

            if (results.length === 0) {
                resultsContainer.innerHTML = `
                    <div style="text-align: center; color: var(--text-grey); padding: 40px;">
                        <i class="fa-solid fa-ghost" style="font-size: 2rem; color: var(--primary-green); margin-bottom: 15px;"></i>
                        <p>No results found for "<strong>${rawQuery}</strong>".</p>
                    </div>`;
                return;
            }

            resultsContainer.innerHTML = results.map((item, index) => {
                const delay = index * 0.05;
                let downHTML = '';
                if (item.file) downHTML += `<a href="${item.file}" target="_blank" class="download-btn"><i class="fa-solid fa-file-pdf"></i> Download DMS vs. DSC white paper</a>`;
                if (item.files) item.files.forEach(f => { downHTML += `<a href="${f.url}" target="_blank" class="download-btn"><i class="fa-solid fa-file-pdf"></i> ${f.label}</a>`; });
                let relHTML = item.related ? `<div style="margin-top: 8px;"><button class="relevance-btn" onclick="openRelevanceGraph('${item.term}')"><i class="fa-solid fa-project-diagram"></i> Relevance</button></div>` : '';
                
                return `
                    <div class="result-card" style="animation-delay: ${delay}s">
                        <div class="term-header">
                            <h3 class="term-title">${highlightText(item.term, query)}</h3>
                            <span class="term-category">${highlightText(item.category, query)}</span>
                        </div>
                        <p class="term-desc">${highlightText(item.desc, query)}</p>
                        ${relHTML}
                        ${downHTML}
                    </div>
                `;
            }).join('');
        }

        // Live Keystroke listener instead of waiting for "Enter"
        searchInput.addEventListener('input', performSearch);
        
        clearBtn.addEventListener('click', () => {
            searchInput.value = ''; searchInput.focus(); performSearch();
        });

        // --- GRAPH LOGIC ---
        window.openRelevanceGraph = function(termName) {
            const termData = terminologyDB.find(t => t.term === termName);
            if (!termData || !termData.related) return;

            document.getElementById('modalChildExplanation').classList.remove('active');
            document.getElementById('graphMasterNode').innerText = termData.term;

            const dist1 = termData.related || [];
            const allRelatedTermsSet = new Set(dist1);
            dist1.forEach(d1 => {
                const d1Data = terminologyDB.find(t => t.term === d1);
                if (d1Data && d1Data.related) d1Data.related.forEach(d2 => { if (d2 !== termName) allRelatedTermsSet.add(d2); });
            });

            const allRelated = Array.from(allRelatedTermsSet);
            const clusters = [], visited = new Set();

            allRelated.forEach(term => {
                if (!visited.has(term)) {
                    const cluster = [], queue = [term];
                    visited.add(term);
                    while (queue.length > 0) {
                        const curr = queue.shift();
                        cluster.push(curr);
                        const currData = terminologyDB.find(t => t.term === curr);
                        if (currData && currData.related) {
                            currData.related.forEach(n => {
                                if (allRelated.includes(n) && !visited.has(n)) { visited.add(n); queue.push(n); }
                            });
                        }
                    }
                    clusters.push(cluster);
                }
            });

            clusters.forEach(c => c.sort((a,b) => (terminologyDB.find(t=>t.term===a)?.category||'').localeCompare((terminologyDB.find(t=>t.term===b)?.category||''))));
            clusters.sort((a,b) => (terminologyDB.find(t=>t.term===a[0])?.category||'').localeCompare((terminologyDB.find(t=>t.term===b[0])?.category||'')));

            const grouped = clusters.flat();
            const relatedNodesContainer = document.getElementById('graphRelatedNodes');
            relatedNodesContainer.innerHTML = '';

            grouped.forEach(rTerm => {
                const n = document.createElement('div');
                n.className = 'round-node node-related';
                if (!dist1.includes(rTerm)) n.classList.add('node-dist2');
                n.innerText = rTerm; n.dataset.term = rTerm;
                n.onclick = (e) => { if (hasGraphDragged) return; showChildTerm(rTerm); };
                relatedNodesContainer.appendChild(n);
            });

            document.getElementById('relevanceModal').classList.add('active');

            setTimeout(() => {
                const vp = document.getElementById('graphViewport').getBoundingClientRect();
                const ct = document.getElementById('graphContainer').getBoundingClientRect();
                const mn = document.getElementById('graphMasterNode').getBoundingClientRect();
                
                document.getElementById('graphContainer').style.transform = 'translate(0,0)';
                
                graphTranslateX = (vp.width * 0.3) - (mn.left - ct.left + mn.width/2);
                graphTranslateY = (vp.height * 0.5) - (mn.top - ct.top + mn.height/2);
                
                document.getElementById('graphContainer').style.transform = `translate(${graphTranslateX}px, ${graphTranslateY}px)`;
                drawLines();
                
                if (document.fonts) document.fonts.ready.then(() => drawLines());
            }, 50);
        };

        function drawLines() {
            const svg = document.getElementById('graphLines');
            svg.innerHTML = '';
            const cRect = document.getElementById('graphContainer').getBoundingClientRect();
            const getCenter = (node) => { const r = node.getBoundingClientRect(); return { x: r.left - cRect.left + r.width/2, y: r.top - cRect.top + r.height/2 }; };
            
            const mNode = document.getElementById('graphMasterNode');
            const mCenter = getCenter(mNode);
            const mData = terminologyDB.find(t => t.term === mNode.innerText);
            const d1Terms = mData?.related || [];
            const nodes = Array.from(document.querySelectorAll('.node-related'));
            const drawn = new Set();

            nodes.forEach(n => {
                if (d1Terms.includes(n.dataset.term)) {
                    const nc = getCenter(n);
                    const l = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    l.setAttribute('x1', mCenter.x); l.setAttribute('y1', mCenter.y);
                    l.setAttribute('x2', nc.x); l.setAttribute('y2', nc.y);
                    l.setAttribute('stroke', 'rgba(255,255,255,0.15)'); l.setAttribute('stroke-width', '2');
                    svg.appendChild(l);
                }
            });

            nodes.forEach(na => {
                const da = terminologyDB.find(t => t.term === na.dataset.term);
                if (da && da.related) {
                    da.related.forEach(tb => {
                        const nb = nodes.find(n => n.dataset.term === tb);
                        if (nb) {
                            const key = [na.dataset.term, tb].sort().join('|');
                            if (!drawn.has(key)) {
                                drawn.add(key);
                                const ca = getCenter(na), cb = getCenter(nb);
                                const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                                const midX = Math.max(ca.x, cb.x) + (Math.abs(ca.y - cb.y) * 0.35);
                                const midY = (ca.y + cb.y) / 2;
                                p.setAttribute('d', `M ${ca.x} ${ca.y} Q ${midX} ${midY} ${cb.x} ${cb.y}`);
                                p.setAttribute('stroke', 'rgba(255,255,255,0.15)'); p.setAttribute('stroke-width', '2'); p.setAttribute('fill', 'none');
                                svg.appendChild(p);
                            }
                        }
                    });
                }
            });
        }

        window.showChildTerm = function(name) {
            const d = terminologyDB.find(t => t.term === name);
            if (!d) return;
            const b = document.getElementById('modalChildExplanation');
            b.innerHTML = `<div style="font-weight:700; color:#2AF598; margin-bottom:5px;">${d.term}</div><div style="font-size:0.95rem; color:#A0AEC0;">${d.desc}</div><button class="see-details-btn" onclick="masterSearch('${d.term}')">See Details <i class="fa-solid fa-arrow-right"></i></button>`;
            b.classList.add('active');
        };

        window.closeModal = function() { document.getElementById('relevanceModal').classList.remove('active'); };
        
        // --- COMPLETELY FIXED "SEE DETAILS" LOGIC ---
        // Instead of reloading the parent URL and breaking the Streamlit iframe,
        // it seamlessly updates the internal text box and live searches instantly!
        window.masterSearch = function(name) {
            closeModal();
            const searchInput = document.getElementById('searchInput');
            searchInput.value = name;
            performSearch();
            window.scrollTo({ top: 0, behavior: 'smooth' }); // Scrolls back to the top to see results
        };

        // Mascot mouse tracking
        document.addEventListener('mousemove', (e) => {
            const mascotImg = document.getElementById('mascotImage');
            if (!mascotImg || mascotImg.classList.contains('jumping-heart')) return;
            const x = (e.clientX / window.innerWidth - 0.5) * 40; 
            const y = (e.clientY / window.innerHeight - 0.5) * -40; 
            const translateX = (e.clientX / window.innerWidth - 0.5) * 15;
            mascotImg.style.transform = `rotateY(${x}deg) rotateX(${y}deg) translateX(${translateX}px)`;
        });

        // Pan Logic
        const vp = document.getElementById('graphViewport');
        const ct = document.getElementById('graphContainer');
        vp.onmousedown = (e) => { isGraphDragging = true; hasGraphDragged = false; graphStartX = e.clientX - graphTranslateX; graphStartY = e.clientY - graphTranslateY; };
        window.onmousemove = (e) => { if(isGraphDragging) { if(Math.abs(e.clientX - graphStartX - graphTranslateX)>3 || Math.abs(e.clientY - graphStartY - graphTranslateY)>3) hasGraphDragged = true; graphTranslateX = e.clientX - graphStartX; graphTranslateY = e.clientY - graphStartY; ct.style.transform = `translate(${graphTranslateX}px, ${graphTranslateY}px)`; } };
        window.onmouseup = () => isGraphDragging = false;
        vp.onclick = (e) => { if(!hasGraphDragged && !e.target.closest('.node-related') && !document.getElementById('modalChildExplanation').contains(e.target)) document.getElementById('modalChildExplanation').classList.remove('active'); };
    </script>
</body>
</html>
"""

# Inject the highly complex interactive component directly into Streamlit
# We set a large height with scrolling to accommodate all searches fluidly
components.html(html_content, height=1200, scrolling=True)
