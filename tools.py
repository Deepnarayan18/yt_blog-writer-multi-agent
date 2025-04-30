from crewai_tools import YoutubeChannelSearchTool

# Configure YouTube tool with HuggingFace embeddings
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@krishnaik06',
    config={
        "embedder": {
            "provider": "huggingface",
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2",
                "model_kwargs": {"device": "cpu"},
                "vector_dimension": 384
            }
        }
    }
)