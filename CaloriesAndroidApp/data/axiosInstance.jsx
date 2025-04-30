// axios-graphql.js
import axios from 'axios';
import { BASE_URL, GRAPHQL_ENDPOINT } from './endpoints';

/**
 * Creates and configures an Axios instance for GraphQL requests
 * @param {string} uri - The GraphQL endpoint
 * @param {Object} options - Additional configuration options
 * @returns {Object} - The configured GraphQL client
 */
const createGraphQLClient = (uri, options = {}) => {
  // Create a new Axios instance with custom config
  const axiosInstance = axios.create({
    baseURL: GRAPHQL_ENDPOINT,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    },
    ...options.axiosConfig
  });

  // Add authentication token if provided
  if (options.token) {
    axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${options.token}`;
  }
  console.log('GraphQL Client created with URI:', uri);

  // Add request interceptor for logging or modifying requests
  axiosInstance.interceptors.request.use(
    config => {
      // You can log requests or modify them here
      return config;
    },
    error => {
      return Promise.reject(error);
    }
  );

  // Add response interceptor for handling common errors
  axiosInstance.interceptors.response.use(
    response => {
      // Handle GraphQL errors that are returned with a 200 status
      if (response.data.errors) {
        const error = new Error('GraphQL Error');
        error.graphQLErrors = response.data.errors;
        return Promise.reject(error);
      }
      return response;
    },
    error => {
      // Handle network or server errors
      return Promise.reject(error);
    }
  );

  /**
   * Execute a GraphQL query or mutation
   * @param {string} query - The GraphQL query/mutation string
   * @param {Object} variables - The variables for the query
   * @param {Object} requestConfig - Additional Axios request config
   * @returns {Promise} - The query result
   */
  const executeQuery = async (query, variables = {}, requestConfig = {}) => {
    try {
      const response = await axiosInstance.post('', {
        query,
        variables
      }, requestConfig);
      
      return response.data.data;
    } catch (error) {
      // Format and rethrow error
      if (error.graphQLErrors) {
        console.error('GraphQL Errors:', error.graphQLErrors);
      } else if (error.response) {
        console.error('Server Error:', error.response.status, error.response.data);
      } else {
        console.error('Error:', error.message);
      }
      throw error;
    }
  };

  return {
    client: axiosInstance,
    query: executeQuery
  };
};

// Usage example
export default createGraphQLClient;