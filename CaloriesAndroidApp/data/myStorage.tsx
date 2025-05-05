import { Platform } from "react-native";
import * as SecureStorage from "expo-secure-store";

const isWeb = Platform.OS === "web";


const Storage = {
    getItem(key: string): string | null {
      return isWeb ? localStorage.getItem(key) : SecureStorage.getItem(key);
    },
  
    setItem(key: string, value: string): void {
      return isWeb
        ? localStorage.setItem(key, value)
        : SecureStorage.setItem(key, value);
    },
  
    async deleteItemAsync(key: string): Promise<void> {
      if (isWeb) {
        localStorage.removeItem(key);
      } else {
        await SecureStorage.deleteItemAsync(key);
      }
    },
  };


export default Storage;