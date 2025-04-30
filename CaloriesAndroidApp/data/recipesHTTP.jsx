import axios from 'axios';

import { RECIPE_DETAIL_ENFDPOINT, RECIPE_LIST_ENFDPOINT, getFullUrl } from './endpoints';



async function fetch_recipes() {
    const endpoint = getFullUrl(RECIPE_LIST_ENFDPOINT);
    console.log('Fetching recipes from:', endpoint);
    try {
        const response = await axios.get(endpoint);
        const data = response.data;
        console.log('Fetched recipes:', data);
        return data.results;
    } catch (error) {
        console.error('Error fetching recipes:', error);
    }
}


async function fetch_recipes_by_id(id) {
    const endpoint = getFullUrl(RECIPE_DETAIL_ENFDPOINT) + `${id}/`;
    try {
        const response = await axios.get(endpoint);
        const data = response.data;
        console.log('Fetched recipe by ID:', data);
        return data;
    } catch (error) {
        console.error('Error fetching recipe by ID:', error);
    }
}


export {
    fetch_recipes,
    fetch_recipes_by_id
}