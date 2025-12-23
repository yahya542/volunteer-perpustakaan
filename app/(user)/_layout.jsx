import { Stack } from "expo-router";

export default function AuthLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="FirstScreen" />
      <Stack.Screen name="Login" />
      <Stack.Screen name="DataPertama" />
      <Stack.Screen name="DataKedua" />
      <Stack.Screen name="Register" />
      <Stack.Screen name="Otp" />
      <Stack.Screen name="LupaSandiScreen" />
    </Stack>
  );
}


