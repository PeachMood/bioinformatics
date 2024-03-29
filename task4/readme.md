# 🔬 Домашнее задание

## Тема

Визуализация структуры белка

## Ссылки

Программное обеспечение: [RasMol](http://www.openrasmol.org/)

Белок: [1AV1](https://www.rcsb.org/structure/1AV1)

## Визуализация

### Начало работы

Для визуализации структуры белка необходимо предварительно:

1. Установить RasMol на устройство
2. Открыть приложение
3. Загрузить белок при помощи команды в терминале `load <filename>`, где `<filename>` - абсолютный путь до файла со структурой белка

В результате в окне приложения должна появиться загруженная структура

![RasMol - Window example](./RasMol%20-%20Window%20example.png)

И терминал для ввода команд

![RasMol - Terminal example](./RasMol%20-%20Terminal%20example.png)

### Wireframe

Wireframe визуализация представляет белок как набор связанных линий, образующих его трехмерную структуру. Этот вид визуализации часто используется для быстрого обзора общей формы белка.

Соответствующую визуализацию можно получить двумя способами.

**Графический интерфейс:**

1. В навигационной панеле приложения выберите _"Display"_
2. Далее из предложеного списка выберите _"Wireframe"_

**Командная строка:**

1. Введите в терминале команду `wireframe on`

![Wireframe - Monochrome](./Wireframe%20-%20Monochrome.png)

### Backbone

Визуализация основы белка показывает только атомы внутреннего скелета белка, исключая боковые цепи. Она подчеркивает общую структуру белка и может использоваться для анализа важных элементов, таких как α-спирали и β-листы.

Соответствующую визуализацию можно получить двумя способами.

**Графический интерфейс:**

1. В навигационной панеле приложения выберите _"Display"_
2. Далее из предложеного списка выберите _"Backbone"_

**Командная строка:**

1. Введите в терминале команду `backbone on`

![Backbone - Monochrome](./Backbone%20-%20Monochrome.png)

### Spacefill + Цветовая модель CPK

Пространственная модель отображает белок с учетом размеров и формы каждого атома. Это позволяет более подробно рассмотреть взаимное расположение атомов внутри белка

Соответствующую визуализацию можно получить двумя способами.

**Графический интерфейс:**

1. В навигационной панеле приложения выберите _"Display"_
2. Далее из предложеного списка выберите _"Spacefill"_
3. Вернитесь к навигационной панеле и выберите _"Colors"_
4. Далее из предложеного списка выберите _"CPK"_

**Командная строка:**

1. Введите в терминале команду `spacefill on`
2. Далее введите команду `color cpk`

![Spacefill - CPK](./Spacefill%20-%20CPK.png)

### Ribbons + Раскраска по доменам белка

Визуализация в виде лент позволяет выделить вторичную структуру белка, такую как α-спирали и β-листы, представляя их в виде лент, обрамляющих центральный химический скелет белка. Это полезно для анализа структурных мотивов.

Соответствующую визуализацию можно получить двумя способами.

**Графический интерфейс:**

1. В навигационной панеле приложения выберите _"Display"_
2. Далее из предложеного списка выберите _"Ribbons"_
3. Вернитесь к навигационной панеле и выберите _"Colors"_
4. Далее из предложеного списка выберите _"Structure"_

**Командная строка:**

1. Введите в терминале команду `ribbons on`
2. Далее введите команду `color structure`

![Ribbons - Structure](./Ribbons%20-%20Structure.png)

### Molecular surface + Temperature (для красоты)

Молекулярная поверхность представляет белок как оболочку, которая отображает области, доступные для взаимодействия с другими молекулами, такими как лиганды или субстраты. Она позволяет анализировать активные участки белка, где могут происходить химические реакции.

Соответствующую визуализацию можно получить через графический интерфейс:

1. В навигационной панеле приложения выберите _"Display"_
2. Далее из предложеного списка выберите _"Molecular surface"_
3. Вернитесь к навигационной панеле и выберите _"Colors"_
4. Далее из предложеного списка выберите _"Temperature"_

![Molecular surface - Temperature](./Molecular%20surface%20-%20Temperature.png)

## Визуализация публикационного качества

Приложение RasMol предоставляет достаточно ограниченный набор функций для визуализации структуры белка, однако, несмотря на это, с его помощью можно получить качественное изображение, подходящее для публикации в журнале:

1. Задайте тип визуализации Strands (аналогично Wireframe, Backbone, Spacefill или Ribbons)
2. Задайте раскраску Temperature (аналогично раскраске Molecular surface)
3. Выберите наиболее удачный ракурс, вращая структуру в графическом интерфейсе
4. Задайте ,белый цвет для фона при помощи команды `background white`
5. Сделайте скриншот получившейся структуры
6. Далее можно улучшить качество изображения при помощи сайта [iLoveIMG](https://www.iloveimg.com/ru/upscale-image)
7. Добавьте красивую надпись в фотошопе
8. Готово ✨

![Molecular surface - Temperature](./Publication%20quality%20image.png)
