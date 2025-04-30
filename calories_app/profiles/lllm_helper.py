import ollama
from decimal import Decimal

def llm_sentence_analysis(sentence):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "user", 
             "content": sentence,
             "system": "You are a helpful assistant that analyzes user's sentences and returns a clearly answer. "
             "You should return a json object with the following keys: User weight: 82 kg, Age: 39, Gender: Male and height: 175 cm"
             "Focus to return the suggested value of calories, protein, carbs and fats depending on the user's goal",
             }
        ]
    )

    return response['message']['content']



def mifflin_st_jeor_bmr(weight, height, age, gender):
    print(weight, height, age, gender)
    
    """
    Calculate BMR using the Mifflin-St Jeor Equation
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in centimeters
    age (int): Age in years
    gender (str): 'male' or 'female'
    
    Returns:
    float: BMR in calories per day
    """
    if gender.lower() == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'f':
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")


def harris_benedict_bmr(weight, height, age, gender):
    """
    Calculate BMR using the Revised Harris-Benedict Equation
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in centimeters
    age (int): Age in years
    gender (str): 'male' or 'female'
    
    Returns:
    float: BMR in calories per day
    """
    if gender.lower() == 'm':
        return Decimal(13.397) * weight + Decimal(4.799) * height - Decimal(5.677) * age + Decimal(88.362)
    elif gender.lower() == 'f':
        return Decimal(9.247) * weight + Decimal(3.098) * height - Decimal(4.330) * age + Decimal(447.593)
    else:
        raise ValueError("Gender must be 'male' or 'female'")

def katch_mcardle_bmr(weight, body_fat_percentage):
    """
    Calculate BMR using the Katch-McArdle Formula
    
    Parameters:
    weight (float): Weight in kilograms
    body_fat_percentage (float): Body fat percentage as a value between 0 and 100
    
    Returns:
    float: BMR in calories per day
    """
    # Convert body fat percentage to decimal
    body_fat_decimal = body_fat_percentage / 100
    lean_body_mass = weight * (1 - body_fat_decimal)
    
    return 370 + 21.6 * lean_body_mass

