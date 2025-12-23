import { useRouter } from "expo-router";
import { useEffect, useRef } from "react";
import { Animated, Image, StyleSheet, Text, View } from "react-native";

const FirstScreen = () => {
  const router = useRouter();

  const opacity = useRef(new Animated.Value(0)).current;
  const scale = useRef(new Animated.Value(0.9)).current;

  useEffect(() => {
    Animated.parallel([
      Animated.timing(opacity, {
        toValue: 1,
        duration: 1200,
        useNativeDriver: true,
      }),
      Animated.spring(scale, {
        toValue: 1,
        friction: 6,
        useNativeDriver: true,
      }),
    ]).start();

    const timer = setTimeout(() => {
      router.replace("/(user)/Login");
    }, 5000);

    return () => clearTimeout(timer);
  }, [router, opacity, scale]);

  return (
    <View style={styles.container}>
      <Animated.View
        style={[
          styles.imageWrapper,
          {
            opacity,
            transform: [{ scale }],
          },
        ]}
      >
        <Image
          source={require("../../assets/images/monumen.png")}
          style={styles.image}
          resizeMode="contain"
        />
        <Text style={styles.label}>PERPUSTAKAAN</Text>
        <Text style={styles.label}>PAMEKASAN</Text>
      </Animated.View>
    </View>
  );
};

export default FirstScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f0f0f0",
    justifyContent: "center",
    alignItems: "center",
  },
  imageWrapper: {
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    width: 320,
    height: 500,
  },
  label: {
    fontSize: 22,
    fontWeight: "800",
    letterSpacing: 1,
    color: "#6A5AE0",
    textShadowColor: "rgba(0,0,0,0.25)",
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
});
