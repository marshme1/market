import java.util.*;

class Toy {
    private String id;
    private String name;
    private int weight;

    public Toy(String id, String name, int weight) {
        this.id = id;
        this.name = name;
        this.weight = weight;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getWeight() {
        return weight;
    }
}

public class ToyRaffle {
    private PriorityQueue<Toy> toyQueue;

    public ToyRaffle() {
        toyQueue = new PriorityQueue<>(Comparator.comparingInt(Toy::getWeight).reversed());
    }

    public void addToy(String id, String name, int weight) {
        toyQueue.add(new Toy(id, name, weight));
    }

    public Toy drawToy() {
        int totalWeight = totalWeight();
        int randomValue = new Random().nextInt(totalWeight);
        int currentWeight = 0;

        for (Toy toy : toyQueue) {
            currentWeight += toy.getWeight();
            if (currentWeight > randomValue) {
                return toy;
            }
        }
        return null; // если ничего не выбрано, что не должно случиться
    }

    private int totalWeight() {
        int weight = 0;
        for (Toy toy : toyQueue) {
            weight += toy.getWeight();
        }
        return weight;
    }

    public static void main(String[] args) {
        ToyRaffle raffle = new ToyRaffle();
        raffle.addToy("1", "Кукла", 5);
        raffle.addToy("2", "Машинка", 3);
        raffle.addToy("3", "Конструктор", 2);
        raffle.addToy("4", "Автобус", 1);
        raffle.addToy("5", "Трактор", 10);
        raffle.addToy("6", "Конфеты", 2);
        raffle.addToy("7", "Телефон", 6);
        raffle.addToy("8", "Компас", 1);
        raffle.addToy("9", "Дед мороз", 4);
        raffle.addToy("10", "Инвалид-колясочник", 8);

        // Проведем 10 розыгрышей
        for (int i = 0; i < 10; i++) {
            Toy drawnToy = raffle.drawToy();
            System.out.println("Выпала игрушка: " + drawnToy.getName());
        }
    }
}
