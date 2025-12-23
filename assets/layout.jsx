import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack screenOptions={{ headerShown: false }} >
      {/* <Stack.Screen name="HomePage" /> */}
    </Stack>
  );
}

// import { Redirect } from 'expo-router';

// export default function InitialRedirect() {
//   return <Redirect href="/user/FirstScreen" />;
// }