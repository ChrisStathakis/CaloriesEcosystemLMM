import React, {useState, useContext, useEffect} from 'react';
import {View, Text} from 'react-native';

import {RootContext, initialState} from '@/data/contextData';
import baseStyle from '../styles/baseStyles';


export default function DayCaloriesComponent() {
    const rootContext_ = useContext(RootContext);
    const selectedDate = rootContext_.selectedDate;
    const dayCalories = rootContext_.dayCalories;
 


    return (
        <Text style={baseStyle.div}>
            <Text style={baseStyle.text_info}>
                Date: {dayCalories.date}
            </Text>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_title}>
                        Calories: {dayCalories.calories}
                    </Text>
                </View>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_title}>
                        Calories: {dayCalories.calories}
                    </Text>
                </View>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_title}>
                        Carbs: {dayCalories.carbs}
                    </Text>
                </View>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_title}>
                        Fats: {dayCalories.fats}
                    </Text>
                </View>
            </Text>
    )

}