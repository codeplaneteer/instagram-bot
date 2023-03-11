interface Item {
    value: number;
    weight: number;
  }
  
  const fractionalKnapsack =(capacity: number, items: Item[]): number =>{
    items.sort((a, b) => b.value / b.weight - a.value / a.weight); // sort items by value/weight ratio in descending order
    let totalValue = 0;
    for (const item of items) {
      if (capacity === 0) break; // if the knapsack is full, exit the loop
      if (item.weight <= capacity) { // if the item can fit in the knapsack, take it completely
        totalValue += item.value;
        capacity -= item.weight;
      } else { // if the item doesn't fit, take a fraction of it
        const fraction = capacity / item.weight;
        totalValue += fraction * item.value;
        capacity = 0;
      }
    }
    return totalValue;
  }
  
  // Example usage
  const knapsackCapacity = 50;
  const items = [
    { value: 60, weight: 10 },
    { value: 100, weight: 20 },
    { value: 120, weight: 30 },
  ];
  const totalValue = fractionalKnapsack(knapsackCapacity, items);
  console.log(`The maximum total value of items that can be carried is: ${totalValue}`); // output: The maximum total value of items that can be carried is: 240