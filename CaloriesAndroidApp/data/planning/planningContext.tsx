import React, { createContext, useReducer } from 'react';


const SET_DATE = 'SET_DATE';

const initialState = {
    selectedDate: '',
}


const selectDateReducer = (state: any, action: any) => {
    switch (action.type) {
        case SET_DATE:
            return { ...state, selectedDate: action.payload };
        default:
            return state;
    }
}

const PlanningContext = createContext(initialState)

export const PlanningProvider = ({ children }: any) => {
    const [state, dispatch] = useReducer(selectDateReducer, {selectDate: ""});
    return (
        <PlanningContext.Provider value={{ state, dispatch }}>
            {children}
        </PlanningContext.Provider>
    )
}