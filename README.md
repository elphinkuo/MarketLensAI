# WheelBrain – Driving Intelligence to New Frontiers

Imagine a world where driving isn’t just autonomous but also exceptionally intelligent, safe and adaptive. That’s what WheelBrain brings to the table.  Welcome to the future of smarter driving.


## Inspiration

With years of experience in the autonomous driving industry, I've witnessed firsthand the challenges and possibilities that lie at the intersection of intelligent transportation and cutting-edge technology. The transformative potential of large language models (LLMs) with multimodal capabilities, such as Llama Vision 3.2, coupled with the unparalleled processing speed of the SambaNova API, sparked the vision for WheelBrain. These advancements inspired me to imagine a universal autonomous driving platform where real-time decision-making and adaptability across diverse environments aren't just goals but inherent capabilities.

The inspiration for WheelBrain also stems from a broader realization: the limitations of existing systems in integrating diverse data streams—visual, textual, and sensory—into a unified, actionable intelligence. The ability to dynamically synthesize this data in real time is not just a leap forward for autonomous driving but a paradigm shift for intelligent agents in general. By bridging human-like contextual understanding with machine precision, WheelBrain aspires to redefine intelligent transportation, creating a platform that is not only adaptive and safe but also visionary in its capacity to transform industries beyond driving.

Ultimately, WheelBrain is driven by the belief that true innovation lies in solving complex, high-stakes problems through elegant, adaptive systems. This vision extends far beyond autonomous vehicles, inspiring possibilities for AI agents to revolutionize fields such as fintech and payment technology. WheelBrain is not just a response to current challenges—it is a glimpse into the limitless potential of intelligent, multimodal AI systems.


## What it does

WheelBrain is a next-generation autonomous driving agent that merges the groundbreaking multimodal capabilities of Llama 3.2 with the unparalleled speed of the SambaNova API. By harnessing advanced reasoning and planning capabilities, it excels at interpreting complex driving scenarios and dynamically adapting to diverse environments in real time. With its ability to process visual, textual, and contextual data simultaneously, WheelBrain provides an intelligent, holistic understanding of the driving landscape. This enables the agent to make rapid, accurate, and context-aware decisions, ensuring seamless navigation in challenging and dynamic settings. Its innovative architecture redefines the standards for autonomous vehicles, pushing the boundaries of what is achievable in AI-powered transportation.

Beyond autonomous driving, WheelBrain’s transformative capabilities hold immense promise for applications in fintech. The platform's ability to integrate multimodal inputs and reason in real time can revolutionize payment technologies, fraud detection, and personalized financial services. For instance, by processing real-time transactional data alongside user behavior and environmental cues, WheelBrain could enable smarter, more secure payment authentication and fraud prevention. These capabilities position it as a trailblazing AI agent with the potential to enhance decision-making and operational efficiency in financial ecosystems, paving the way for a smarter, more connected future across industries.

## Implementation

We implemented a Python-based solution to visualize driving paths on road images using SambaNova API using the model Llama-3.2-11B-Vision-Instruct.

The solution begins by initializing the OpenAI client with the necessary API key and base URL. This setup allows the script to interact with the OpenAI API for generating driving path descriptions. A function is defined to read an image file and return its base64 encoded string, which is required to send the image data to the OpenAI API.

A prompt is crafted to instruct the AI model to analyze the provided road image and generate a driving path. The prompt asks the AI to draw a driving path on the image and provide the coordinates of the path. The script sends a request to the OpenAI API using the Llama-3.2-11B-Vision-Instruct model, including the prompt and the base64 encoded image.

The API responds with a description of the driving path and the coordinates. The coordinates extracted are used to plot the driving path on the original image.

The matplotlib library is utilized to display the image with the overlaid driving path, providing a visual representation of the AI-generated navigation. This solution demonstrates how to leverage AI models to generate and visualize driving paths on road images. The script interacts with the OpenAI API to obtain driving path descriptions and coordinates, which are then plotted on the images for visualization.

This approach can be extended to various applications in autonomous driving and driver assistance systems. By generating accurate driving paths, the solution can aid in the development of more sophisticated navigation systems. Additionally, the solution can be integrated with other AI models to improve its performance and accuracy.

The use of AI models to generate driving paths has the potential to revolutionize the field of autonomous driving. With the ability to analyze images and generate accurate navigation paths, AI models can help reduce the risk of accidents and improve overall road safety. As the technology continues to evolve, we can expect to see more advanced applications of AI-generated driving paths in the future.

### Autonomous Driving Environment Simulation Implementation

This section details our approach using CARLA and SUMO simulators in a co-simulation setup, providing a comprehensive testing environment for autonomous driving algorithms.

#### CARLA Simulation

CARLA (Car Learning to Act) stands as one of the leading open-source simulators for autonomous driving research. It provides a highly realistic 3D environment built on Unreal Engine, offering high-fidelity graphics and physics simulation. The platform enables researchers to simulate complex urban driving scenarios with detailed vehicle dynamics, environmental conditions, and sensor implementations including cameras, LiDAR, and radar systems. In our implementation, CARLA provides three distinct camera perspectives:

* A front-left camera view, offering visibility of the left-side approach  
* A front-right camera view, covering the right-side approach  
* A central front camera view, providing direct forward visibility

These multiple viewpoints enable comprehensive perception of the vehicle's surroundings, crucial for autonomous driving decision-making.

#### SUMO Simulation

SUMO (Simulation of Urban MObility) represents a microscopic traffic simulation package designed to handle large road networks. As an open-source traffic simulation suite, SUMO excels in modeling intricate traffic patterns, pedestrian movements, and public transport systems. In our setup, SUMO provides a Bird's Eye View (BEV) perspective of the entire traffic scenario, offering a comprehensive overhead view of all vehicle movements and interactions within the simulation environment. This macro-level visualization is particularly valuable for understanding traffic flow patterns and vehicle distributions across the network.

#### CARLA-SUMO Co-simulation

The integration of CARLA and SUMO creates a powerful co-simulation environment that leverages the strengths of both platforms. A key feature of our implementation is the precise synchronization between CARLA's three camera views and SUMO's BEV perspective. This synchronization ensures that all visualizations represent the exact same moment in the simulation, allowing researchers to simultaneously observe both detailed vehicle-level interactions through CARLA's cameras and the broader traffic patterns through SUMO's overhead view.

![][image1]

[Simulation Video](https://vimeo.com/1032191948)

#### Technical Implementation Details

Our implementation leverages high-performance computing resources and specific software configurations to ensure optimal simulation performance. The setup utilizes two NVIDIA 3090TI GPUs, providing substantial computational power for handling the complex rendering and physics calculations required by the simulation environment.

The simulation environment operates through a distributed architecture, with CARLA running on the localhost at port 2000 and SUMO operating on port 8813\. Both simulators are configured to use the Town05 map, which provides a consistent environmental layout across both platforms. This shared map environment ensures that the spatial relationships and road networks are identical between CARLA's detailed 3D environment and SUMO's traffic simulation.

The synchronization mechanism between CARLA and SUMO operates on multiple levels:

* Temporal synchronization ensures that all camera views and the BEV perspective represent the same exact moment in time  
* Spatial synchronization maintains consistent vehicle positions across both simulators  
* Traffic flow synchronization ensures that vehicle movements, traffic patterns, and interactions are identical in both CARLA's camera views and SUMO's BEV perspective

This multi-layered synchronization creates a coherent simulation environment where researchers can simultaneously observe:

* Detailed front-view perspectives from three different angles through CARLA's cameras  
* A comprehensive overhead view of the entire traffic scenario through SUMO's BEV  
* Perfectly matched traffic flows and vehicle behaviors across all viewpoints

The implementation specifically uses CARLA version 0.9.14 or higher and SUMO version 1.15.0 or higher, ensuring compatibility and stable operation of the synchronized multi-view system. The Town05 map, utilized in both simulators, provides a diverse urban environment featuring various road types, intersections, and traffic scenarios, making it ideal for comprehensive autonomous driving testing and validation.

### WheelBrain Agent Drives in the Carla-SUMO co-simulated Environment

The WheelBrain system implements a sophisticated vision-language driving agent that operates within a co-simulated environment combining CARLA and SUMO simulators. At its core, WheelBrain leverages the SambaNova API to process real-time visual data through the Llama-3.2-11B-Vision-Instruct model, enabling comprehensive scene understanding and dynamic decision-making capabilities.

#### Vision-Based Decision Making Architecture

The system's primary component, `SambaNovaVisionAgent`, processes multi-camera inputs from three distinct perspectives: front, front-left, and front-right. These images are encoded in base64 format and combined with contextual information about the driving environment to form a complete situational awareness input. The agent processes this information through a structured prompt that includes:

* Available driving actions  
* Current navigation requirements  
* Ego vehicle state information  
* Current lane configuration and context

The vision-language model analyzes this multi-modal input to generate reasoned driving decisions, following a three-part response framework:

1. Scene Description: Detailed analysis of the visual environment  
2. Reasoning: Explicit decision-making logic based on environmental context  
3. Action Selection: Final behavior choice (e.g., acceleration, deceleration, lane changes)

#### Continuous Learning Framework

WheelBrain incorporates an innovative continuous learning architecture that enhances the base capabilities of the vision-language model. This framework consists of:

* A reflection module that analyzes driving decisions and their outcomes  
* A memory system that maintains a database of driving experiences and their results  
* A feedback loop that incorporates collision detection and safety monitoring

The system stores driving decisions and their contexts in a structured database, enabling post-hoc analysis and performance improvement. Each decision is recorded with comprehensive metadata including token usage, processing time, and outcome metrics.

#### Robust Error Handling and Safety Features

The implementation includes sophisticated error handling mechanisms to manage various driving scenarios:

* Collision prevention through active monitoring  
* Lane change validation and safety checks  
* Deadlock detection and resolution  
* Timeout management for decision-making processes

The system implements a retry mechanism for handling network-related issues, ensuring robust operation even under unstable connectivity conditions. This is particularly crucial for maintaining consistent performance during real-time decision-making processes.

#### Integration with Simulation Environment

The co-simulation setup leverages both CARLA's high-fidelity 3D visualization capabilities and SUMO's efficient traffic simulation features. Key integration points include:

* Synchronized vehicle state management between simulators  
* Coordinated traffic light control  
* Consistent environment state maintenance  
* Real-time visualization through a custom GUI interface

The implementation maintains a step-length of 0.1 seconds for fine-grained control, with major decision points occurring every 10 simulation steps to balance responsiveness with computational efficiency.

## Challenges we ran into

### Data Synchronization:
Combining multimodal data from various sources while maintaining temporal and spatial coherence was a significant challenge. To support the real-time decision-making capabilities of WheelBrain, we developed a robust synchronization framework that harmonized diverse inputs with precision. This framework was critical to ensuring the platform’s ability to process complex scenarios dynamically and adaptively, providing a seamless driving experience even in rapidly changing environments.

### Model Optimization:
Balancing the speed and accuracy of our AI models was another key challenge. We optimized the sampling rate of scene inputs and fine-tuned the request frequency to the lightning-fast SambaNova API to ensure real-time responsiveness. This approach enabled WheelBrain to deliver superior performance without compromising on the quality of its reasoning and planning capabilities.

### Simulation Integration:
Integrating the co-simulation environments of Carla and SUMO with WheelBrain was a complex but rewarding endeavor. By leveraging these simulators and combining their outputs with the real-time responsiveness of the SambaNova API, we validated the platform’s advanced multimodal reasoning and planning capabilities. This integration allowed us to rigorously test the agent in diverse, realistic scenarios, ensuring its readiness for real-world applications.

*** Memory Optimization *** 
Designing an effective memory module for the WheelBrain Agent was pivotal to enhancing its performance as it gained driving experience. This module was carefully crafted to strengthen the agent’s ability to learn while maintaining a balance between leveraging past experience and generalizing to new scenes. This ensures WheelBrain remains adaptive and robust, demonstrating its versatility not only in autonomous driving but also in potential fintech applications where contextual understanding and real-time decision-making are equally critical.


Overcoming these challenges not only strengthened WheelBrain's potential as a state-of-the-art autonomous driving platform but also highlighted its transformative applications in fintech. The same capabilities that enable real-time decision-making and contextual reasoning in driving environments can be leveraged to revolutionize areas such as fraud detection, payment authentication, and personalized financial services. This positions WheelBrain as a versatile AI agent with the promise of reshaping industries beyond transportation.


## Accomplishments that we're proud of

**Real-time Performance**: We successfully reduced the latency of our multimodal data processing, achieving response times suitable for real-world driving applications.

**Adaptive Learning**: Implemented an adaptive reinforcement learning framework that allows WheelBrain to continuously improve from real-world driving scenarios.

**Scalability**: Built a modular and scalable architecture that can be easily expanded or adapted for new sensors and driving environments.