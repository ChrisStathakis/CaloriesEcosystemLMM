import {View, Text, StyleSheet} from "react-native";
import React from "react";

import { fetch_recipes_by_id } from "../../data/recipesHTTP";

export default function RecipeDetail() {
    const [recipe, setRecipe] = React.useState({title: ""});

    React.useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetch_recipes_by_id(1); // Fetch recipe with ID 1
                setRecipe(data);
            } catch (error) {
                console.error("Error fetching recipe:", error);
            }
        };

        fetchData();

    }, []);


    return (
        <View style={styles.container}>
            <Text>{recipe.title}</Text>
        </View>
    )


}

const styles = StyleSheet.create({
    container: {
        flex: 1
    }
})
