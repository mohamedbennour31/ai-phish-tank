import ollama

def analyze_phish(image_path, target_url):
    print("[*] Sending screenshot to AI for analysis...")
    
    prompt_text = f"""Analyze this image for cybersecurity risks. 
    1. Does this look like a login page? 
    2. What brand is it attempting to represent? 
    3. The actual URL is '{target_url}'. On a scale of 1-10, how likely is this to be a phishing page? 
    Compare the visual brand identity against the provided URL."""

    response = ollama.generate(
        model='llava',
        prompt=prompt_text,
        images=[image_path]
    )

    print("\n--- AI ANALYSIS REPORT ---")
    print(response['response'])
