from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_id = 'google/flan-t5-large'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=50  # Adjust the max_length according to your requirements
)

question = input("Enter your question: ")

result = pipe(question)[0]['generated_text']
print("Result:", result)
print("End of program")

