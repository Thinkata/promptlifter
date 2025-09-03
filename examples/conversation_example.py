#!/usr/bin/env python3
"""
Example usage of the new ConversationLLM interface.

This script demonstrates how to use the simplified conversation-focused
interface for PromptLifter.
"""

import asyncio
import os
import sys

# Add the parent directory to the path so we can import promptlifter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from promptlifter import ConversationConfig, ConversationLLM, quick_chat


async def basic_conversation_example() -> None:
    """Basic conversation example."""
    print("=== Basic Conversation Example ===")

    # Initialize with default config
    llm = ConversationLLM()

    # Chat examples
    response1 = await llm.chat("What is machine learning?")
    print(f"User: What is machine learning?")
    print(f"Assistant: {response1.message}")
    print(f"Sources: {response1.context_sources}")
    print(f"Tokens: {response1.tokens_used}")
    print()

    response2 = await llm.chat("Can you give me an example?")
    print(f"User: Can you give me an example?")
    print(f"Assistant: {response2.message}")
    print(f"Sources: {response2.context_sources}")
    print(f"Tokens: {response2.tokens_used}")
    print()

    # Get conversation stats
    stats = llm.get_conversation_stats()
    print(f"Conversation stats: {stats}")
    print()


async def custom_config_example() -> None:
    """Example with custom configuration."""
    print("=== Custom Configuration Example ===")

    # Custom configuration
    config = ConversationConfig(
        max_history_tokens=2000,
        max_context_tokens=1000,
        enable_auto_search=True,
        search_relevance_threshold=0.8,
        system_prompt="You are a helpful research assistant. Provide detailed, accurate responses.",
    )

    llm = ConversationLLM(config)

    response = await llm.chat("Explain quantum computing in simple terms")
    print(f"User: Explain quantum computing in simple terms")
    print(f"Assistant: {response.message}")
    print(f"Sources: {response.context_sources}")
    print()


async def quick_chat_example() -> None:
    """Example using the quick_chat function."""
    print("=== Quick Chat Example ===")

    # Simple one-off chat
    response = await quick_chat("What are the benefits of renewable energy?")
    print(f"Quick chat response: {response}")
    print()


async def conversation_management_example() -> None:
    """Example of conversation management features."""
    print("=== Conversation Management Example ===")

    llm = ConversationLLM()

    # Start a conversation
    await llm.chat("Hello, I'm interested in learning about AI")
    await llm.chat("What are the main types of AI?")
    await llm.chat("Can you explain machine learning specifically?")

    # Get conversation stats
    stats = llm.get_conversation_stats()
    print(f"After 3 messages - Stats: {stats}")

    # Export conversation
    history = llm.export_conversation()
    print(f"Exported {len(history)} conversation turns")

    # Clear conversation
    llm.clear_conversation()
    stats_after_clear = llm.get_conversation_stats()
    print(f"After clearing - Stats: {stats_after_clear}")

    # Import conversation back
    llm.import_conversation(history)
    stats_after_import = llm.get_conversation_stats()
    print(f"After importing - Stats: {stats_after_import}")
    print()


async def configuration_example() -> None:
    """Example of configuration management."""
    print("=== Configuration Management Example ===")

    llm = ConversationLLM()

    # Get current config
    config = llm.get_config()
    print(f"Current config: {config}")

    # Update config
    llm.update_config(max_history_tokens=3000, enable_auto_search=False)

    # Get updated config
    updated_config = llm.get_config()
    print(f"Updated config: {updated_config}")

    # Get retrieval and optimization stats
    retrieval_stats = llm.get_retrieval_stats()
    optimization_stats = llm.get_optimization_stats()
    print(f"Retrieval stats: {retrieval_stats}")
    print(f"Optimization stats: {optimization_stats}")
    print()


async def main() -> None:
    """Run all examples."""
    print("PromptLifter ConversationLLM Examples")
    print("=" * 50)

    try:
        await basic_conversation_example()
        await custom_config_example()
        await quick_chat_example()
        await conversation_management_example()
        await configuration_example()

        print("All examples completed successfully!")

    except Exception as e:
        print(f"Error running examples: {e}")
        print("Make sure you have configured your environment variables properly.")
        print("See env.example for required configuration.")


if __name__ == "__main__":
    asyncio.run(main())
