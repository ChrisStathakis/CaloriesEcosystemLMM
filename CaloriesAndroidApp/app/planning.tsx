import React, { useState, useEffect } from 'react';
import {View, Text, Button, StyleSheet} from 'react-native';

import { fetch_day_calorie_list, fetch_day_calorie_detail } from '../data/planning/index';


export default function PlanningScreen() {
    const [dayCalories, setDayCalories] = useState(null);
    const [recipes, setRecipes] = useState(null);
    const [dayCategories, setDayCategories] = useState(null);
    const [userRecipes, setUserRecipes] = useState(null);

    useEffect(() => { 
        
        const fetchDayCalories = async () => {
            const response = await fetch_day_calorie_list();
            setDayCalories(response);
        }
        
        fetchDayCalories
    }, [])


}