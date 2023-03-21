import openai
import streamlit as st

# Step 1: Obtain OpenAI API key

openai.api_key = "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"


def translatemandarinetoenglish(model, prompt):
    chat = openai.ChatCompletion.create(
        model=model,
        messages=prompt
    )
    reply = chat['choices'][0]['message']['content']
    return reply


def main():
    st.set_page_config(page_title="GPT 中译英工具", page_icon=":guardsman:", layout="wide")
    st.title("GPT 中译英工具")
    st.markdown("请根据您的需求，由 GPT 帮助您翻译内容。")

    # Get user input
    Translate_content = st.text_area("输入需要翻译的内容:")

    prompt = [
        {"role": "system", "content": "你是个翻译专家."},
        {"role": "user", "content": f"请回答：{Translate_content} "}
    ]

    model = "gpt-3.5-turbo"

    if st.button("翻译"):
        translate = translatemandarinetoenglish(model, prompt)
        st.success("大功告成！")
        st.markdown(translate)


if __name__ == "__main__":
    main()
