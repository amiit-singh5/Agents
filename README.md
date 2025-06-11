# Agents
AI opensource Agentic  approach:
An agentic approach in AI involves designing systems (agents) that can perceive their environment, reason logically, and take actions to achieve goals autonomously.
The perceive method means the agent is sensing or recognizing an input (stimulus) from the environment (like "hungry" or "bored") and deciding what action to take based on its internal logic (the rules dictionary).

**The main advantages of the AI agentic approach are:**
    1. Autonomy: Agents can make decisions without constant human intervention.
    2. Goal-directed behavior: They can pursue specific objectives in dynamic environments.
    3. Adaptability: They can adjust actions based on changes in their environment.
    4. Modular design: Agents can be combined to build complex systems.
    5. Reusability: Individual agents can be reused in different contexts.
In short: AI agents can think, act, and react logically in their environment, making them highly effective for automation and problem-solving.

**Key components of the AI agentic approach are:**
    1. Perception/Sensing — to gather data from the environment.
    2. Knowledge Base — to store facts, rules, or models.
    3. Reasoning/Decision-making — to choose the best action logically.
    4. Action/Execution — to carry out decisions and affect the environment.
    5. Goals/Objectives — define what the agent aims to achieve.
    6. Learning (optional) — to improve performance over time.
Together, these components enable the agent to sense, reason, and act in a dynamic environment.
In the agentic approach, the AI component is the part that uses logical reasoning to decide the best action based on its knowledge base and goals.
For example:
    • The rules dictionary  represents the knowledge base.
    • The decision logic  is the AI component that reasons and chooses actions.
In other words, AI is the "brain" that makes decisions in the agent.

**list of major frameworks and tools to develop agentic systems:**
    1. Python Libraries
        ◦ spade: Multi-agent systems in Python
        ◦ gym / stable-baselines3: Reinforcement learning agents
        ◦ CrewAI: Collaborative LLM-based agents
        ◦ ray[rllib]: Scalable RL agents
    2. Java-based Frameworks
        ◦ JADE: Java Agent DEvelopment Framework
        ◦ Jason: AgentSpeak interpreter for BDI agents
    3. Robotics and Simulations
        ◦ ROS (Robot Operating System): For robotics agents
        ◦ Unity ML-Agents: Training agents in 3D environments
        ◦ Webots: Robotics simulation
    4. Logic Programming
        ◦ Prolog: Logic-based agents
        ◦ Drools: Rule-based decision systems (Java)
    5. Deep Learning Frameworks
        ◦ TensorFlow and PyTorch: Build AI agents with neural networks
    6. Other
        ◦ Microsoft Bot Framework: For conversational agents
        ◦ Dialogflow: NLP-based agents (Google)
        ◦ Rasa: Open-source conversational agents
Note:
    • Python is the most versatile for both logic and learning-based agents.
    • Choose a framework based on your goals (rule-based, learning, conversational, robotics, etc.).
Y

ou can write an agentic system in pure Python (or any language) without using a framework by manually coding:
    1. Perception — using inputs (e.g., sensor data, user input).
    2. Knowledge Base — storing facts, rules, or conditions in variables or dictionaries.
    3. Reasoning — using if-else, loops, or logic-based structures to make decisions.
    4. Actions — defining functions to perform actions.


**Open-Source AI Models for Decision-Making in Agentic Systems:**
    1. Reinforcement Learning Models
        ◦ Stable-Baselines3 (SB3) — Pre-trained policies (DQN, PPO, A2C).
        ◦ RLlib — OpenAI Baselines models for various tasks.
    2. Large Language Models (LLMs) for Reasoning & Planning
        ◦ GPT-4 (OpenAI, via API) — Decision-making via prompt engineering.
        ◦ LLaMA 3 (Meta) — Reasoning via prompt chains or fine-tuning.
        ◦ Vicuna, Mistral, OpenHermes — Smaller open LLMs for logical reasoning.
    3. Behavioral Cloning Models
        ◦ BCQ (Batch-Constrained Q-learning) — Pre-trained models in some research repos.
    4. Planning and Control
        ◦ RoboPlanner — Pre-trained models for robot navigation (ROS-based).
        ◦ LlamaIndex — Chain-of-thought reasoning via pre-trained language models.
    5. Logic-based Reasoners
        ◦ DeepProbLog — Combines neural nets with probabilistic logic.
        ◦ ProbLog — Probabilistic logic programming, pre-trained rule sets.


**Proprietary AI Models for Agentic Systems:**
    1. OpenAI GPT (e.g., GPT-4, GPT-4o) — LLMs capable of reasoning, decision-making, and planning via prompts or API.
    2. Google Gemini (formerly Bard) — LLMs with decision-making and reasoning abilities.
    3. Anthropic Claude — A safe, scalable conversational model that can make decisions through prompt engineering.
    4. Microsoft Copilot — Powered by OpenAI models, useful for decision support.
    5. IBM Watson Assistant — Virtual assistant with decision trees and reasoning modules.
    6. Amazon Bedrock (Titan, Claude) — Managed generative AI services for building agents.
    7. NVIDIA Omniverse AI — Simulation and reinforcement learning for robotic agents.
    8. Palantir Foundry AI — Integrates decision-making AI into business logic.
    9. SAP AI Core — Integrates AI agents into business processes.
    10. DataRobot — Offers AutoML with decision support capabilities.


