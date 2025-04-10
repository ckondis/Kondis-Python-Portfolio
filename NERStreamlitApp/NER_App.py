import streamlit as st #Imports streamlit package
import spacy #Imports spaCy package for NLP and NER
import pandas as pd #Imports pandas package
import io #Imports io package

st.set_page_config(page_title="Custom NER with spaCy", layout="wide") #Sets the page title and layout

st.title("🔍 Named Entity Recognition (NER) with SpaCy") #Inputs the app title
st.write("""
    Welcome to the Named Entity Recognition (NER) app powered by spaCy! This tool allows you to explore 
    the process of identifying named entities in text and creating custom patterns to detect specific 
    entities based on your needs. Here's how it works:

    1. **spaCy's NER Pipeline**: 
        - spaCy uses a pre-trained pipeline to analyze text and automatically recognize named entities, 
        such as people, organizations, dates, locations, and more.
        - It works by processing the text through several stages, including tokenization, part-of-speech tagging, 
         and ultimately identifying named entities.

    2. **Creating Custom Patterns**: 
        - With this tool, you can define custom patterns for specific entity labels.
        - For example, you can create a pattern to detect different types of dogs (e.g., "Golden Retriever", "Poodle") 
        by defining the label DOG and providing a list of matching patterns.
        - Once your patterns are added, spaCy's EntityRuler component will incorporate them into the pipeline and 
        help identify your custom entities in the text.

    3. **How the Works**: 
        - You can either enter your own text or upload a document, and the app will analyze it to detect both 
        built-in spaCy entities and any custom entities you have defined.
        - Custom entities will be highlighted in the text and shown in the "Detected Named Entities" section with 
        their labels and descriptions.

    Let's start by defining custom entities or using one of the sample texts below!
""") #Displays a brief description of how the app works

nlp = spacy.load("en_core_web_sm") #Loads pre-trained spaCy model 

if "patterns" not in st.session_state: #Initializes session for custom patterns
    st.session_state.patterns = []

st.sidebar.header("🛠️ Define Custom Entity Rules") #Creates header for sidebar section
with st.sidebar.form("custom_entity_form"): #Creates a form in the sidebar
    label = st.text_input("Entity Label (e.g., ELECTRONICS, PLANT)") #Text box for user input in entity label
    description = st.text_input("Description for Label (optional)") #User input in entity description
    pattern_text = st.text_input("Pattern(s) to Match (e.g., 'Television, Phone')") #User input in entity pattern
    st.caption("👉 To add multiple patterns, separate them with commas. (e.g., tree, tulip, grass)") #Adds text caption
    submitted = st.form_submit_button("➕ Add Rule") #Interactive button to submit custom rules

    if submitted and label and pattern_text: 
        pattern_list = [p.strip().lower() for p in pattern_text.split(",") if p.strip()] #Make patterns lowercase
        for p in pattern_list: #Iterates over each pattern
            st.session_state.patterns.append({ 
                "label": label.upper(),   #Converts label to uppercase format
                "description": description, #Saves description
                "pattern": p  #Save each individual pattern
            })
        st.success(f"Added {len(pattern_list)} pattern(s) under label: {label.upper()}") #Displays success message

if st.session_state.patterns: #Checks if there are custom patterns saved
    with st.expander("📋 Current Custom Rules"): #Forms an expandable table
        # Create a DataFrame for display
        df = pd.DataFrame(st.session_state.patterns) #Convert patterns to a DataFrame
        df['description'] = df['description'].fillna("No description available")  #Identify/label missing descriptions
        st.table(df) #Displays the DataFrame

st.subheader("📝 Try a Sample or Upload Your Own Text") #Displays sub-header

col1, col2, col3 = st.columns(3) #Creates 3 columns for sample text buttons

if "sample_text" not in st.session_state: #Checks if sample text exists
    st.session_state.sample_text = "" #Initializes sample text if not present

if col1.button("📊 Company Example"): #If company sample text button selected display text
    st.session_state.sample_text = "Google and Tesla are leading tech companies based in the United States, known for innovation and rapid growth."

if col2.button("🏛️ History Example"): #If history sample text button selected display text
    st.session_state.sample_text = "On July 20, 1969, Neil Armstrong became the first person to walk on the Moon during the Apollo 11 mission."

if col3.button("📅 Work Schedule Example"): #If work sample text button selected display text
    st.session_state.sample_text = "Alex works Monday to Friday from 9 AM to 5 PM at the downtown office, with meetings every Tuesday and Thursday."

uploaded_file = st.file_uploader("📂 Upload a .txt file", type=["txt"]) #Provides file uploader to users for text files
st.subheader("Write your text here or use a sample:") #Displays sub-header
text_area_input = st.text_area("", value=st.session_state.sample_text, height=200) #Text area for user input of text

analyze = st.button("🔍 Analyze Text") #Submit button to analyze the text


if analyze or uploaded_file: # If Analyze button is clicked
    # Load uploaded text if available
    if uploaded_file:
        stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8")) #Read file content
        text = stringio.read() #Store text from file
    else:
        text = text_area_input #Otherwise use input text in provided text area
    if "custom_ruler" in nlp.pipe_names: #Check if custom_ruler exists in spaCy's pipeline
        nlp.remove_pipe("custom_ruler") #Remove it if it exists

    if st.session_state.patterns: #If custom pattern exists
        ruler = nlp.add_pipe("entity_ruler", name="custom_ruler", before="ner") #Add custom entity ruler
        ruler.add_patterns(st.session_state.patterns) #Add the custom patterns to the entity ruler

    doc = nlp(text) # Process the text through spaCy's NER pipeline

    st.subheader("📌 Detected Named Entities") #Display subheader
    if doc.ents: #Checks if any entities are detected in the text
        for ent in doc.ents: #Loops through each detected entity
            explanation = spacy.explain(ent.label_) or "No description available" #Display entity description or no description text
            custom_entity = next((item for item in st.session_state.patterns if item["label"] == ent.label_), None) #Checks for custom description defined by the user
            if custom_entity: #If a custom description exists
                explanation = custom_entity["description"] if custom_entity["description"] else "No description available" #Use custom description or say none exists
                st.markdown(f"- **{ent.text}** — _{ent.label_}_ ({explanation})", unsafe_allow_html=True) #Display entity with custom description 
            else:
                st.markdown(f"- **{ent.text}** — _{ent.label_}_ ({explanation})") #Display entity without custom description
    else:
        st.info("No named entities detected.") #Display message if no detected entities


    st.subheader("🎨 Highlighted Entities in Text") #Display subheader

    def highlight_entities(text, doc): #Function to highlight entities in the text
        colors = { #Define color mapping for different entity types
            "PERSON": "#ffcccb",  # red
            "ORG": "#c3e6cb",     # green
            "GPE": "#add8e6",     # blue
            "DATE": "#ffe0b2",    # peach
            "TIME": "#e0bbff",    # purple
            "MONEY": "#d1f0ff",   # light blue
            "PRODUCT": "#f4cccc", # pink
            "EVENT": "#d9ead3",   # soft green
            "LOC": "#fff2cc",     # yellow
            "FAC": "#e6f7ff",     # cyan
            "LANGUAGE": "#f9cb9c" # orange
        }

        highlighted = "" #Initialize an empty string to store highlighted text
        last_end = 0 #Track position of last processed character in the text
        for ent in doc.ents: #Loop through each detected entity in document
            color = colors.get(ent.label_, "#d3d3d3") #Get entity color based on label type
            if ent.label_ in [rule["label"] for rule in st.session_state.patterns]:  # If a custom pattern highlight with orange color
                color = "#FFA500"  # Orange for custom entities
            highlighted += text[last_end:ent.start_char] 
            highlighted += ( #Highlight the entity text with its color and display text
                f"<span style='background-color:{color}; padding:2px 4px; border-radius:4px;'>"
                f"<b>{ent.text}</b> ({ent.label_})</span>"
            ) #Display entity text with label in bold
            last_end = ent.end_char #Update the position of the last processed character to the end of the current entity
        highlighted += text[last_end:] #Add remaining text after last entity
        return highlighted #Return highlighted version of the text

    st.markdown(highlight_entities(text, doc), unsafe_allow_html=True) #Render text with HTML format