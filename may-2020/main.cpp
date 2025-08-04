#include <iostream>
#include <vector>
#include <algorithm>

template <typename T>
void printVector(const std::vector<T>& v) {
  std::cout << "[";
  for (const auto& elem : v)
    std::cout << elem << " ";
  std::cout << "]" << std::endl;
}

int main (int argc, char *argv[]) {
  std::vector<int> row;
  int new_number = 19;
  for (int i = 1; i < new_number; i++) {
    row.push_back(i);
  }
  int elementToFind = 11;
  int iteration = 1;
  while (true) {
    auto it = std::find(row.begin(), row.end(), elementToFind);
    if (it == row.end()) {
      std::cout << "Iteration: " << iteration - 1 << std::endl;
      break;
    }
    while (row.size() < iteration + iteration) row.push_back(new_number++);
    std::vector<int> first_part(row.begin(), row.begin() + iteration - 1);
    std::vector<int> second_part(row.begin() + iteration, row.begin() + iteration + iteration - 1);
    row.erase(row.begin(), row.begin() + first_part.size() + second_part.size() + 1); 
    std::vector<int> new_beginning;
    for (const auto& _ : first_part) {
      new_beginning.insert(new_beginning.begin(), second_part.back());
      second_part.pop_back();
      new_beginning.insert(new_beginning.begin(), first_part.front());
      first_part.erase(first_part.begin());
    }
    row.insert(row.begin(), new_beginning.begin(), new_beginning.end());
    iteration++;
  }
  return 0;
}
