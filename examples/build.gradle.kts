plugins {
    kotlin("jvm") version "2.1.0"
    java
}

group = "tests"
version = "1.0"

repositories {
    mavenCentral()
}

kotlin {
    jvmToolchain(21)
}

sourceSets {
    main {
        kotlin {
            srcDirs("src/main/kotlin")
        }
        java {
            srcDirs("src/main/java")
        }
    }
}
