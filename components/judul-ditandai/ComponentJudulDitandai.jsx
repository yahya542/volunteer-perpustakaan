import { useEffect, useState } from "react";
import {
  FlatList,
  Image,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import Delete from "../../assets/icons/Delete.png";

const ComponentJudulDitandai = () => {
  const [bookmarks, setBookmarks] = useState([]);
  const [isDeleteMode, setIsDeleteMode] = useState(false);
  const [selectedIds, setSelectedIds] = useState([]);

  useEffect(() => {
    fetchBookmarks();
  }, []);

  const fetchBookmarks = async () => {
    try {
      const response = await fetch(
        "https://9dec003548aa.ngrok-free.app/api/bookmarks/"
      );
      const data = await response.json();
      setBookmarks(data);
    } catch (error) {
      console.error("Error fetching bookmarks:", error);
      setBookmarks([]);
    }
  };

  const toggleSelect = (id) => {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id]
    );
  };

const handleDeleteSelected = async () => {
  try {
    for (const id of selectedIds) {
      await fetch(`https://9dec003548aa.ngrok-free.app/api/bookmarks/${id}`, {
        method: "DELETE",
      });
    }

    fetchBookmarks();

    setSelectedIds([]);
    setIsDeleteMode(false);
  } catch (error) {
    console.error("Error deleting bookmarks:", error);
  }
};


  const renderBookmark = ({ item }) => {
    const isSelected = selectedIds.includes(item.id);

    return (
      <TouchableOpacity
        onPress={() => {
          if (isDeleteMode) toggleSelect(item.id);
        }}
        style={[
          styles.bookmarkItem,
          isDeleteMode && isSelected ? styles.selectedItem : {},
        ]}
      >
        <Image source={{ uri: item.cover }} style={styles.cover} />
        <View style={styles.info}>
          <Text style={styles.title}>{item.title}</Text>
          <Text style={styles.author}>by {item.author}</Text>
        </View>
        {isDeleteMode && (
          <Text style={[styles.checkmark, { color: isSelected ? "red" : "#ccc" }]}>
            ✔
          </Text>
        )}
      </TouchableOpacity>
    );
  };

  return (
    <View style={styles.container}>
      <View style={{ alignItems: "center", width: "100%" }}>
        <View style={styles.countContainer}>
          <View style={styles.countBadge}>
            <Text style={styles.countText}>
              {bookmarks.length} daftar judul saat ini
            </Text>
          </View>
          <TouchableOpacity onPress={() => setIsDeleteMode(!isDeleteMode)}>
            <Image source={Delete} style={{ marginLeft: 10 }} />
          </TouchableOpacity>
        </View>
      </View>

      {bookmarks.length === 0 ? (
        <View style={styles.noData}>
          <Text>Tidak ada data</Text>
        </View>
      ) : (
        <FlatList
          data={bookmarks}
          keyExtractor={(item) => item.id.toString()}
          renderItem={renderBookmark}
          contentContainerStyle={styles.list}
          showsVerticalScrollIndicator={true}
        />
      )}

      {isDeleteMode && selectedIds.length > 0 && (
        <TouchableOpacity style={styles.confirmButton} onPress={handleDeleteSelected}>
          <Text style={styles.confirmText}>✔ Hapus {selectedIds.length} Buku</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};

export default ComponentJudulDitandai;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "100%",
  },
  countContainer: {
    marginTop: 20,
    alignItems: "center",
    width: "100%",
    flexDirection: "row",
    justifyContent: "center",
  },
  countBadge: {
    backgroundColor: "#664BD1",
    height: 25,
    width: 208,
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 30,
  },
  countText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 14,
  },
  noData: {
    marginTop: 20,
    alignItems: "center",
    justifyContent: "center",
  },
  list: {
    paddingHorizontal: 20,
    paddingTop: 20,
  },
  bookmarkItem: {
    flexDirection: "row",
    backgroundColor: "#fff",
    padding: 10,
    borderRadius: 10,
    marginBottom: 10,
    alignItems: "center",
  },
  selectedItem: {
    borderColor: "red",
    borderWidth: 2,
  },
  cover: {
    width: 80,
    height: 100,
    borderRadius: 8,
    marginRight: 10,
  },
  info: {
    flex: 1,
  },
  title: {
    fontSize: 16,
    fontWeight: "bold",
    marginBottom: 4,
  },
  author: {
    fontSize: 14,
    color: "#666",
  },
  checkmark: {
    fontSize: 24,
    marginLeft: 10,
  },
  confirmButton: {
    backgroundColor: "green",
    padding: 10,
    borderRadius: 30,
    alignItems: "center",
    margin: 20,
  },
  confirmText: {
    color: "white",
    fontWeight: "bold",
  },
});