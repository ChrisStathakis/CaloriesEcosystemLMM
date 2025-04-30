import { Text, View, StyleSheet, FlatList } from 'react-native';
import React, { useEffect, useState } from 'react';
import { Image } from 'expo-image';

import MyButton from '../../components/ui_components/button';
import { Pressable, TextInput } from 'react-native-gesture-handler';
import { fetch_recipes } from '../../data/recipesHTTP';
import baseStyle from "../../components/styles/baseStyles";

const PlaceholderImage = require('@/assets/images/recipes.jpg');

export default function RecipesPage() {
  const [showSearchModal, setSearchModal] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [recipes, setRecipes] = useState([]);


  useEffect(() => {
    const fetchData = async () => {
      try {
      const data = await fetch_recipes();
      if (data !== undefined) {setRecipes(data)}
      console.log('use effect recipes:', data);
      
      } catch (error) {
      console.error('Error fetching recipes:', error);
      }
    };

    fetchData();
   
  }, []);

  const handleRecipePress = (id) => {
    console.log('Recipe ID:', id);
    // Navigate to the new component or perform any action with the id
  };

  const renderRecipeItem = ({ item }) => (
    <View onClick={()=> {handleRecipePress(item.id)}} style={styles.tableRow}>
      <Text style={styles.tableCell}>{item.title}</Text>
      <Text style={styles.tableCell}>{item.calories}</Text>
      <Text style={styles.tableCell}>{item.protein}</Text>
      <Text style={styles.tableCell}>{item.fats}</Text>
      <Text style={styles.tableCell}>{item.carbs}</Text>
      <Pressable style={baseStyle.baseButton}>Details</Pressable>
    </View>
  );

  return (
    <View>
      <View style={styles.container}>
        <Image
          source={PlaceholderImage}
          style={{ width: 200, height: 200 }}
        />
        <Text style={styles.text}>Recipes Page</Text>
        <Text style={styles.text}>Search Recipes</Text>
        <MyButton title="Search" onPress={() => setSearchModal(true)} />
        {showSearchModal ? (
          <View>
            <Text style={styles.text}>Search Recipes</Text>
            <TextInput
              placeholder="Search for recipes..."
              value={searchText}
              onChangeText={setSearchText}
              style={{ borderWidth: 1, padding: 10, width: 200 }}
            />
          </View>
        ) : null}
      </View>

      {/* Table Header */}
      <View style={styles.tableHeader}>
        <Text style={styles.tableHeaderCell}>Title</Text>
        <Text style={styles.tableHeaderCell}>Calories</Text>
        <Text style={styles.tableHeaderCell}>Protein</Text>
        <Text style={styles.tableHeaderCell}>Fats</Text>
        <Text style={styles.tableHeaderCell}>Carbs</Text>
        <Text style={styles.tableHeader}>-</Text>
      </View>

      {/* Table Body */}
      <FlatList
        data={recipes}
        renderItem={renderRecipeItem}
        keyExtractor={(item, index) => index.toString()}
        style={styles.table}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  text: {
    fontSize: 24,
    color: '#333',
  },
  table: {
    margin: 10,
  },
  tableHeader: {
    flexDirection: 'row',
    backgroundColor: '#ddd',
    padding: 10,
  },
  tableHeaderCell: {
    flex: 1,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  tableRow: {
    flexDirection: 'row',
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
    padding: 10,
  },
  tableCell: {
    flex: 1,
    textAlign: 'center',
  },
});