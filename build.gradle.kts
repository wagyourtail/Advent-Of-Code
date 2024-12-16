plugins {
    kotlin("jvm") version "2.1.0"
}

repositories {
    maven("https://maven.wagyourtail.xyz/snapshots")
    mavenCentral()
}

dependencies {
    implementation("xyz.wagyourtail.commons:commons-kt:1.0.2-SNAPSHOT")
    implementation("org.apache.commons:commons-math3:3.6.1")
}

for (folder in file("src").listFiles()) {
    sourceSets.create(folder.name) {
        compileClasspath += sourceSets.main.get().compileClasspath
        runtimeClasspath += sourceSets.main.get().runtimeClasspath
    }
}