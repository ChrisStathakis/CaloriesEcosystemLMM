import { createContext } from "react";


export const initialState = {
    selectedDate: new Date().toISOString().split('T')[0],
    dayCalories: {
        date: '',
        protein: 0,
        carbs: 0,
        fats: 0,
        calories: 0,
    }
}

export const RootContext = createContext(initialState);

