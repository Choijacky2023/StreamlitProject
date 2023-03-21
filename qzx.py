import openai
import streamlit as st

# Step 1: Obtain OpenAI API key

openai.api_key = "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"


def generatechildstroy(model, prompt, temperature, max_tokens):
    chat = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    reply = chat['choices'][0]['message']['content']
    return reply


def main():
    st.set_page_config(page_title="GPT 儿童故事绘 OpenAI GPT Child Story", page_icon=":guardsman:", layout="wide")
    st.title("OpenAI GPT 儿童故事绘\nOpenAI GPT Child Story")
    st.markdown("请根据您的要求，由 OpenAI GPT 帮助你生成一段儿童故事。")

    # Get user input
    describe_tone = st.text_area("输入描述语气 Describe Tone:")
    story_character = st.text_area("输入故事主角 Story Character:")
    story_content = st.text_area("输入故事内容 Story Content:")
    prompt = [
        {"role": "system", "content": "你是讲故事很厉害的人."},
        {"role": "user", "content": f"用{describe_tone} 的语气写一段儿童故事:\n故事主角是\n{story_character}，故事内容是\n{story_content}\n"}
    ]

    model = "gpt-3.5-turbo"
    temperature = st.slider("选择随机值 Choose Temperature:", 0.0, 1.0, 0.7)
    max_tokens = st.slider("选择故事长度 Choose Max Tokens:", 50, 2000, 500)

    if st.button("生成故事 Generate"):
        child_story = generatechildstroy(model, prompt, temperature, max_tokens)
        st.success("大功告成！故事已经生成了！\n Success! Your Story is Ready")
        st.markdown(child_story)


if __name__ == "__main__":
    main()
