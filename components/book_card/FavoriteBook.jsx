import React from 'react';
import { View, Text, ScrollView, Image, TouchableOpacity, StyleSheet } from 'react-native';

const books = [
  { id: 1, title: 'Buku 1', cover: require('../../assets/images/img.jpg')},
  { id: 2, title: 'Buku 2', cover: require('../../assets/images/img.jpg') },
  { id: 3, title: 'Buku 3', cover: require('../../assets/images/img.jpg') },
  { id: 4, title: 'Buku 4', cover: require('../../assets/images/img.jpg') },
  { id: 5, title: 'Buku 5', cover: require('../../assets/images/img.jpg') },
  { id: 6, title: 'Buku 6', cover: require('../../assets/images/img.jpg') },
  { id: 7, title: 'Buku 7', cover: require('../../assets/images/img.jpg') },
  { id: 8, title: 'Buku 8', cover: require('../../assets/images/img.jpg') },
];

function FavoriteBook() {
  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Rekomendasi Buku</Text>
      <ScrollView horizontal showsHorizontalScrollIndicator={false}>
        {books.map((book) => (
          <View key={book.id} style={styles.card}>
            <Image source={book.cover} style={styles.image} />
            <Text style={styles.title}>{book.title}</Text>
          </View>
        ))}
        <TouchableOpacity style={styles.moreCard} onPress={() => console.log('Lihat selengkapnya')}>
          <Text style={styles.moreText}>Selengkapnya →</Text>
        </TouchableOpacity>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 20,
    paddingLeft: 16,
  },
  heading: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  card: {
    marginRight: 12,
    alignItems: 'center',
    width: 100,
  },
  image: {
    width: 100,
    height: 150,
    borderRadius: 8,
  },
  title: {
    marginTop: 6,
    fontSize: 14,
    textAlign: 'center',
  },
  moreCard: {
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 16,
  },
  moreText: {
    fontSize: 14,
    color: '#007AFF',
    fontWeight: 'bold',
  },
});

export default FavoriteBook;