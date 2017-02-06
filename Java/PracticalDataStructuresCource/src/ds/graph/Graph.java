package ds.graph;

import java.util.ArrayList;

/**
 * Created by blakfeld on 2/6/17.
 */
public class Graph {

    private int vCount;  // Num of Vertices.
    private int eCount;  // Num of Edges.

    private ArrayList[] adjacents;

    public Graph(int vCount) {
        this.vCount = vCount;
        this.eCount = 0;
        adjacents = new ArrayList[vCount];

        for (int i = 0; i < vCount; i++) {
            adjacents[i] = new ArrayList();
        }
    }

    public int getVertexCount() {
        return vCount;
    }

    public int getEdgeCount() {
        return eCount;
    }

    public void addEdge(int src, int dest) {
        adjacents[src].add(dest);
        eCount++;
    }

    public Object[] adj(int src) {
        return adjacents[src].toArray();
    }
}
