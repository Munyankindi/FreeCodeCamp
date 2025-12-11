full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Validate the character name
    if not isinstance(name, str):
        return 'The character name should be a string.'
    if len(name) > 10:
        return 'The character name is too long.'
    if ' ' in name:
        return 'The character name should not contain spaces.'
    
    # Validate the stats
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers.'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1.'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4.'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points.'
    
    # Format the output
    str_representation = f"{name}\n"
    str_representation += f"STR {'●' * strength}{'○' * (10 - strength)}\n"
    str_representation += f"INT {'●' * intelligence}{'○' * (10 - intelligence)}\n"
    str_representation += f"CHA {'●' * charisma}{'○' * (10 - charisma)}"
    
    return str_representation

# Example usage
result = create_character("ren", 4, 2, 1)
print(result)
