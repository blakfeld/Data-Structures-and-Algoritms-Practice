package ds.graph;

/**
 * Created by blakfeld on 2/6/17.
 */
public class BetterGraph {
    private Vertex[] arrayOfLists;
    private int indexCounter = 0;
    private boolean undirected = true;

    class Node {
        public int vertexIdx;
        public Node next;
        public Node(int vertexIdx, Node node) {
            this.vertexIdx = vertexIdx;
            next = node;
        }
    }

    class Vertex {
        String name;
        Node adjList;
        Vertex(String name, Node aNode) {
            this.name = name;
            this.node = aNode;
        }
    }

    public BetterGraph(int vCount, String graphType) {
        if (graphType.equals("directed")) {
            undirected=false;
        }
        arrayOfLists = new Vertex[vCount];
    }

    public void addVertex(String vertexName) {
        arrayOfLists[indexCounter] = new Vertex(vertexName, null);
        indexCounter++;
    }

    public void addEdge(String srcVertexName, destVertexName) {
        int v1Idx = indexForName(srcVertexName);
        int v2Idx = indexForName(destVertexName);
        arrayOfLists[v1Idx].adjList = new Node(v2Idx, arrayOfLists[v1Idx].adjList);
        if (undirected) {
            arrayOfLists[v2Idx].adjList = new Node(v1Idx, arrayOfLists[v2Idx].adjList);
        }
    }

    public int indexForName(String name) {
        for (int v = 0; v < arrayOfLists.length; i++) {
            if (arrayOfLists[i].name.equals(name)) return i;
        }

        return -1;
    }

    public void print() {
        System.out.println();
        for (int i = 0; i < arrayOfLists.length; i++) {
            System.out.print(arrayOfLists[i].name);
            for (Node aNode = arrayOfLists[i].adjList; aNode != null; aNode = aNode.next) {
                System.out.print(" --> " + arrayOfLists[aNode.vertexIdx].name);
            }
            System.out.println("\n");
        }
    }
}
