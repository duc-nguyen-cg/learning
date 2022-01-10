package list;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamList {

    public static void main(String[] args) {
        //print
        List<Integer> list = Arrays.asList(17,33, 58, 23, 11,89,5, 97);
        list.stream().forEach(e -> System.out.print(e+ "   " ));

        System.out.println();

        //filter and collect to new list
        List even = list.stream().filter(num -> num % 2 == 0).collect(Collectors.toList());
        even.stream().forEach(e -> System.out.print(e + "   " ));

        System.out.println();

        //sort
        list.stream().sorted().forEach(e -> System.out.print(e + "   " ));

        System.out.println();

        //concat
        List newList = Stream.concat(list.stream(), Stream.of(33, 101)).collect(Collectors.toList());
        newList.stream().forEach(e -> System.out.print(e + "   "));

        System.out.println();

        //create a newList
        List originList = Stream.of(
                new Person(2L, "Duck", 20, true),
                new Person(1L, "Shikikan", 25, true),
                new Person(5L, "Enty", 22, false)
        ).collect(Collectors.toList());
        originList.stream().forEach(p -> System.out.println(p.toString()));

        //map
        List square = list.stream().sorted().map(x -> x*2).collect(Collectors.toList());
        square.stream().forEach(e -> System.out.print(e + "   "));
    }
}
