import React from "react";
import {
  View,
  Text,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
} from "react-native";

export default function KategoriTema({
  data = [],
  selected,
  onSelect = () => {},
}) {
  return (
    <View style={styles.wrapper}>
      <Text style={styles.title}>Kategori</Text>

      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.scrollContainer}
      >
        {data.map((item) => {
          const active = selected === item.id;
          return (
            <TouchableOpacity
              key={item.id}
              onPress={() => onSelect(item.id)}
              style={[styles.pill, active && styles.pillActive]}
            >
              <Text style={[styles.pillText, active && styles.pillTextActive]}>
                {item.name}
              </Text>
            </TouchableOpacity>
          );
        })}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    marginTop: 10,
    marginBottom: 5,
    height: 70,
  },
  title: {
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 10,
    marginLeft: 10,
  },
  scrollContainer: {
    paddingHorizontal: 10,
  },
  pill: {
    borderWidth: 2,
    borderColor: "#6A4DFE",
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 20,
    marginRight: 10,
  },
  pillActive: {
    backgroundColor: "#6A4DFE",
  },
  pillText: {
    fontSize: 14,
    color: "#6A4DFE",
    fontWeight: "500",
  },
  pillTextActive: {
    color: "white",
  },
});
