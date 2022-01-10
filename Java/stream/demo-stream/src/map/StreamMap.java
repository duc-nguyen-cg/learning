package map;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamMap {
    public static void main(String[] args) {
        Map<Integer, String> testMap = new HashMap<>();
        testMap.put(1, "Azure");
        testMap.put(2, "Peridot");
        testMap.entrySet().stream()
                .forEach(System.out::println);

        System.out.println();
        //get Key
        testMap.entrySet().stream().map(Map.Entry::getKey).forEach(System.out::println);

        System.out.println();

        //get Value
        testMap.entrySet().stream().map(Map.Entry::getValue).forEach(System.out::println);

    }
}
