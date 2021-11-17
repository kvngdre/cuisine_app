import time
import pickle
import pandas as pd
from PIL import Image
import streamlit as st

button_state = None

st.title('Identifying a Cuisine?')
image = Image.open('testimage.jpg')
st.image(image)

y_test = pd.read_csv('https://raw.githubusercontent.com/kvngdre/cuisine_app/main/pred.csv')


options = st.multiselect(label='Enter ingredients below',
                         options=['Almond', 'Anise', 'Anise_seed', 'Apple', 'Apple_brandy', 'Apricot',
                                  'Armagnac', 'Artemisia', 'Artichoke', 'Asparagus', 'Avocado', 'Bacon',
                                  'Baked_potato', 'Banana', 'Barley', 'Bartlett_pear', 'Basil', 'Bay',
                                  'Bean', 'Beech', 'Beef', 'Beef_broth', 'Beef_liver', 'Beer', 'Beet',
                                  'Bell_pepper', 'Bergamot', 'Berry', 'Bitter_orange', 'Black_bean',
                                  'Black_currant', 'Black_mustard_seed_oil', 'Black_pepper',
                                  'Black_raspberry', 'Black_sesame_seed', 'Black_tea', 'Blackberry',
                                  'Blackberry_brandy', 'Blue_cheese', 'Blueberry', 'Bone_oil',
                                  'Bourbon_whiskey', 'Brandy', 'Brassica', 'Bread', 'Broccoli',
                                  'Brown_rice', 'Brussels_sprout', 'Buckwheat', 'Butter', 'Buttermilk',
                                  'Cabbage', 'Cabernet_sauvignon_wine', 'Cacao', 'Camembert_cheese',
                                  'Cane_molasses', 'Caraway', 'Cardamom', 'Carob', 'Carrot', 'Cashew',
                                  'Cassava', 'Catfish', 'Cauliflower', 'Caviar', 'Cayenne', 'Celery',
                                  'Celery_oil', 'Cereal', 'Chamomile', 'Champagne_wine', 'Chayote',
                                  'Cheddar_cheese', 'Cheese', 'Cherry', 'Cherry_brandy', 'Chervil',
                                  'Chicken', 'Chicken_broth', 'Chicken_liver', 'Chickpea', 'Chicory',
                                  'Chinese_cabbage', 'Chive', 'Cider', 'Cilantro', 'Cinnamon', 'Citrus',
                                  'Citrus_peel', 'Clam', 'Clove', 'Cocoa', 'Coconut', 'Coconut_oil',
                                  'Cod', 'Coffee', 'Cognac', 'Concord_grape', 'Condiment', 'Coriander',
                                  'Corn', 'Corn_flake', 'Corn_grit', 'Cottage_cheese', 'Crab',
                                  'Cranberry', 'Cream', 'Cream_cheese', 'Cucumber', 'Cumin',
                                  'Cured_pork', 'Currant', 'Date', 'Dill', 'Eel', 'Egg', 'Egg_noodle',
                                  'Elderberry', 'Emmental_cheese', 'Endive', 'Enokidake', 'Fennel',
                                  'Fenugreek', 'Feta_cheese', 'Fig', 'Fish', 'Flower', 'Frankfurter',
                                  'Fruit', 'Galanga', 'Gardenia', 'Garlic', 'Gelatin', 'Gin', 'Ginger',
                                  'Goat_cheese', 'Grape', 'Grape_brandy', 'Grape_juice', 'Grapefruit',
                                  'Green_bell_pepper', 'Green_tea', 'Gruyere_cheese', 'Guava',
                                  'Haddock', 'Ham', 'Hazelnut', 'Herring', 'Holy_basil', 'Honey', 'Hop',
                                  'Horseradish', 'Huckleberry', 'Jamaican_rum', 'Japanese_plum',
                                  'Jasmine', 'Jasmine_tea', 'Juniper_berry', 'Kaffir_lime', 'Kale',
                                  'Katsuobushi', 'Kelp', 'Kidney_bean', 'Kiwi', 'Kohlrabi', 'Kumquat',
                                  'Lamb', 'Lard', 'Lavender', 'Leaf', 'Leek', 'Lemon', 'Lemon_juice',
                                  'Lemon_peel', 'Lemongrass', 'Lentil', 'Lettuce', 'Licorice',
                                  'Lima_bean', 'Lime', 'Lime_juice', 'Lime_peel_oil', 'Lingonberry',
                                  'Litchi', 'Liver', 'Lobster', 'Long_pepper', 'Lovage',
                                  'Macadamia_nut', 'Macaroni', 'Mace', 'Mackerel', 'Malt', 'Mandarin',
                                  'Mandarin_peel', 'Mango', 'Maple_syrup', 'Marjoram', 'Matsutake',
                                  'Meat', 'Melon', 'Milk', 'Milk_fat', 'Mint', 'Mozzarella_cheese',
                                  'Mung_bean', 'Munster_cheese', 'Mushroom', 'Mussel', 'Mustard',
                                  'Mutton', 'Nectarine', 'Nira', 'Nut', 'Nutmeg', 'Oat', 'Oatmeal',
                                  'Octopus', 'Okra', 'Olive', 'Olive_oil', 'Onion', 'Orange',
                                  'Orange_flower', 'Orange_juice', 'Orange_peel', 'Oregano', 'Ouzo',
                                  'Oyster', 'Palm', 'Papaya', 'Parmesan_cheese', 'Parsley', 'Parsnip',
                                  'Passion_fruit', 'Pea', 'Peach', 'Peanut', 'Peanut_butter',
                                  'Peanut_oil', 'Pear', 'Pear_brandy', 'Pecan', 'Pepper', 'Peppermint',
                                  'Peppermint_oil', 'Pimenta', 'Pimento', 'Pineapple', 'Pistachio',
                                  'Plum', 'Popcorn', 'Porcini', 'Pork', 'Pork_liver', 'Pork_sausage',
                                  'Port_wine', 'Potato', 'Potato_chip', 'Prawn', 'Prickly_pear',
                                  'Provolone_cheese', 'Pumpkin', 'Quince', 'Radish', 'Raisin',
                                  'Rapeseed', 'Raspberry', 'Raw_beef', 'Red_algae', 'Red_bean',
                                  'Red_kidney_bean', 'Red_wine', 'Rhubarb', 'Rice', 'Roasted_almond',
                                  'Roasted_beef', 'Roasted_meat', 'Roasted_peanut', 'Roasted_pork',
                                  'Roasted_sesame_seed', 'Romano_cheese', 'Root', 'Roquefort_cheese',
                                  'Rose', 'Rosemary', 'Rum', 'Rutabaga', 'Rye_bread', 'Rye_flour',
                                  'Saffron', 'Sage', 'Sake', 'Salmon', 'Salmon_roe', 'Sassafras',
                                  'Sauerkraut', 'Savory', 'Scallion', 'Scallop', 'Sea_algae',
                                  'Seaweed', 'Seed', 'Sesame_oil', 'Sesame_seed', 'Shallot',
                                  'Sheep_cheese', 'Shellfish', 'Sherry', 'Shiitake', 'Shrimp', 'Smoke',
                                  'Smoked_salmon', 'Smoked_sausage', 'Sour_cherry', 'Sour_milk',
                                  'Soy_sauce', 'Soybean', 'Spearmint', 'Squash', 'Squid', 'Star_anise',
                                  'Starch', 'Strawberry', 'Strawberry_jam', 'Strawberry_juice',
                                  'Sturgeon_caviar', 'Sumac', 'Sunflower_oil', 'Sweet_potato',
                                  'Swiss_cheese', 'Tabasco_pepper', 'Tamarind', 'Tangerine', 'Tarragon',
                                  'Tea', 'Tequila', 'Thai_pepper', 'Thyme', 'Tomato', 'Tomato_juice',
                                  'Truffle', 'Tuna', 'Turkey', 'Turmeric', 'Turnip', 'Vanilla', 'Veal',
                                  'Vegetable', 'Vegetable_oil', 'Vinegar', 'Violet', 'Walnut', 'Wasabi',
                                  'Watercress', 'Watermelon', 'Wheat', 'Wheat_bread', 'Whiskey',
                                  'White_bread', 'White_wine', 'Whole_grain_wheat_flour', 'Wine',
                                  'Wood', 'Yam', 'Yeast', 'Yogurt', 'Zucchini'], key=0)

if len(options) < 4:
    st.warning('Please enter minimum of four ingredients.')
elif len(options) >= 4 and len(options) < 7:
    st.warning('For improved results please enter minimum of seven ingredients.')
    button_state = st.button('Predict')
else:
    button_state = st.button('Predict')


@st.cache(allow_output_mutation=True)
def loading_model(file):
    model_ = pickle.load(open(file, 'rb'))
    return model_


model_load_state = st.text('Please wait...')
model = loading_model('food_model.pkl')
model_load_state.text('')

if button_state:
    y_test.loc[0, options] = 1

    prediction = model.predict(y_test)

    st.success(f"This cuisine is {prediction[0]} ")
