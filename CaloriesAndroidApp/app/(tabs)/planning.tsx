import React, { useState, useEffect, useContext } from 'react';
import {View, Text, Button, StyleSheet} from 'react-native';
import { fetch_day_calorie_list, fetch_day_calorie_detail, fetch_day_categories, fetch_user_recipes } from '../../data/planning/index';

import baseStyle from "../../components/styles/baseStyles";
import { RootContext } from '../../data/contextData';
import DayCaloriesComponent from '@/components/planning/DayCaloriesComponent';

const dayCaloriesDummy = {
    'date': '',
    'calories': 0,
    'carbs': 0,
    'fats': 0,
    'protein': 0,
};


export default function PlanningScreen() {
    const rootContext = useContext(RootContext);
    const [activeTab, setActiveTab] = useState('Tab1');
    const selectedDate = rootContext.selectedDate;
    const [dayCalories, setDayCalories] = useState(dayCaloriesDummy);
    const [recipes, setRecipes] = useState(null);
    const [dayCategories, setDayCategories] = useState(null);
    const [userRecipes, setUserRecipes] = useState(null);

    useEffect(() => { 
        
        const fetchDayCalories = async () => {
            const response = await fetch_day_calorie_detail(selectedDate);
            const dayCategoriesResponse = await fetch_day_categories(response.id);
            setDayCalories(response);
            setDayCategories(dayCategoriesResponse);
        }
        
        fetchDayCalories();
    }, [])

    const renderContent = () => {
        switch (activeTab) {
            case 'Tab1':
                return <DayCaloriesComponent />;
            case 'Tab2':
                return <Text>Tab 2 Content</Text>;
            case 'Tab3':
                return <Text>Tab 3 Content</Text>;
            default:
                return null;
        }
    }

    return (
        <View style={baseStyle.container}>
            <
        </View>
    )
}