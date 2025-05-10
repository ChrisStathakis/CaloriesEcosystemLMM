import { Stack, Tabs } from "expo-router";
import TabLayout from "./(tabs)/_layout";
import {RootContext, initialState } from "@/data/contextData";



export default function RootLayout() {
  return (
    <RootContext.Provider value={initialState}>
      <Stack>
        <TabLayout />     
      </Stack>
    </RootContext.Provider>
  );
};


